from decimal import Decimal
import stripe
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from apps.orders.models import Order


stripe.api_key = settings.STRIPE_API_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):

    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("payment:completed"))
        cancel_url = request.build_absolute_uri(reverse("payment:canceled"))
        # Stripe checkout session data
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(item.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {
                            "name": item.product.title,
                        },
                    },
                    "quantity": item.quantity,
                }
            )
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                name=order.coupon.code, pracent_off=order.discount, duration="once"
            )
            session_data["discounts"] = [{"coupon": stripe_coupon.id}]
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)

    return render(request, "payment/process.html", locals())


def payment_completed(request):
    return render(request, "payment/completed.html")


def payment_canceled(request):
    return render(request, "payment/canceled.html")
