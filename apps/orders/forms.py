from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "address1",
            "address2",
            "city",
            "postal_code",
            "country_code",
        )
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "lastName",
                    "placeholder": "",
                    "required": "",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "you@example.com",
                    "required": "",
                },
            ),
            "address1": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "address1",
                    "placeholder": "",
                    "required": "",
                },
            ),
            "address2": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "address2",
                    "placeholder": "",
                    "required": "",
                },
            ),
            "city": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "city",
                    "placeholder": "",
                    "required": "",
                },
            ),
            "postal_code": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "postalCode",
                    "placeholder": "",
                    "required": "",
                },
            ),
            "country_code": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "countryCode",
                    "placeholder": "",
                    "required": "",
                },
            ),
        }
