from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get('username')
            password = cd.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"{user.username} you successfully loged - ✅")
                return redirect("shop:home")
            
            messages.warning(request, f"Invalid username(👤) or password(🔑) - ❌")
            return redirect("account:login")
        
        messages.warning(request, f"username or password not found - ❌")
        return redirect("account:login")

    return render(request, "account/login.html", {"form": form})


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully registered in system - ✅, please enter username and password in Login panel 🔑.")
            return redirect("account:login")
        
        messages.warning(request, f"Your registration are not valid or not found- ❌")
        return redirect("account:register")
    
    return render(request, "account/register.html", {"form": form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, f"Successfully loged out - ✅")
    return redirect("account:login")


def profile_user(request, username):
    return render(request, "account/profile.html")