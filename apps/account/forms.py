from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "username...",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "id": "floatPassword",
                "placeholder": "password...",
            }
        )
    )

    class Meta:
        pass


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "first name",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "last name",
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "username",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "class": "form-control rounded-4",
                "id": "floatInput",
                "placeholder": "phone number",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "id": "floatPassword",
                "placeholder": "Password",
            }
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "id": "floatPassword",
                "placeholder": "Password",
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "password",
            "password_confirm",
        )

    def save(self, commit=True):
        user = super().save(commit)

        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Passwords must be match!")
        else:
            user.set_password(password)
            user.save()
