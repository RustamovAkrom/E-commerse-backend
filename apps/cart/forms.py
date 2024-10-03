from django.utils.translation import gettext_lazy as _
from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_("Quantity"),
        widget=forms.NumberInput(attrs={
            "class": "me-2 mt-2 mb-2", "type": "number", "placeholder": "QTY", "value": 1, "min": 1, "max": 100, "height": 100
        })
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
