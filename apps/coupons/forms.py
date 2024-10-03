from django.utils.translation import gettext_lazy as _
from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        label=_("Coupon"),
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control me-2",
                "placeholder": "Promo code",
            }
        ),
    )
