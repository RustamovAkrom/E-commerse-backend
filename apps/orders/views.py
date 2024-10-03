from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from apps.cart.cart import Cart
from apps.coupons.forms import CouponApplyForm
from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created


def order_create(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please authorizate on system.")
        return redirect("account:login")

    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.user = request.user
            order.total_paid = cart.get_total_price_after_discount()
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # clear the cart
            cart.clear()
            # Launch asynchronous task
            # order_created(order.id) #####################
            # set the order in the session
            request.session["order_id"] = order.id
            # redirect for payment
            messages.success(request, "Successfully placed order")
            return redirect("payment:process")
        messages.error(request, "Your field are not valid")

    else:
        form = OrderCreateForm()

    coupon_apply_form = CouponApplyForm()

    return render(
        request,
        "orders/create.html",
        {"cart": cart, "form": form, "coupon_apply_form": coupon_apply_form},
    )


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/detail.html", {"order": order})
