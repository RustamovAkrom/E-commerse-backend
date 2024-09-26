from decimal import Decimal

from django.conf import settings

from apps.checkout.models import DeliveryOptions
from apps.shop.models import Product
from apps.coupons.models import Coupon


class Cart:
    """
    A base Cart class, Providing some default bahvariors that
    can ve inherited or overrided, as necassary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # shop current applied coupon
        self.coupon_id = self.session.get("coupon_id")

    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id] = {"price": str(product.price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and retur products
        """

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item["qty"] for item in self.cart.values())

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item["price"] * item["qty"] for item in self.cart.values()))

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]
            ).delivery_pricel

        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = self.get_subtotal_price()

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]
            ).delivery_price

        total = subtotal + Decimal(newprice)
        return total

    def cart_update_delivery(self, deliveryprice=0):
        subtotal = self.get_subtotal_price()
        total = subtotal + Decimal(deliveryprice)
        return total

    def delete(self, product):
        """
        Delte item from session data
        """
        product_id = str(product.id)

        if product_id in self.session:
            del self.session[product_id]
            self.save()

    def clear(self):
        """
        Remove Cart from session
        """
        del self.session[settings.CART_SESSION_ID]
        # del self.session["address"]
        # del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    
    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal(100) * self.get_total_price())
        return Decimal(0)
    
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
