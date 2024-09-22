from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))

    class Meta:
        pass


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={}))

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
