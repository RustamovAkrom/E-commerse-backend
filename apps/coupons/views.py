from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import CouponApplyForm
from .models import Coupon


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data["code"]
        try:
            coupon = Coupon.objects.get(
                code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True
            )
            request.session["coupon_id"] = coupon.id
            messages.success(request, "Successfully applyed coupon.")
        except Coupon.DoesNotExist:
            request.session["coupon_id"] = None
            messages.warning(request, "Coupon does not exist.")
    return redirect("cart:cart_detail")
