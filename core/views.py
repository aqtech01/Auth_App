from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login_page/")
def home(request):
    # user = User.get_username("username")
    context = {
        "title": "Home",
        "user":request.user.username
    }
    return render(request, "core/home.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Invalid Credentials")

    context = {
        "title": "Login"
    }

    return render(request, "core/login.html", context)


def signup_page(request):
    context = {
        "title": "SignUp"
    }
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            messages.warning(request, "Password or Confirm Password Should be same")
        else:
            user = User.objects.create_user(uname, email, password1)
            user.save()
            return redirect("login_page")

    return render(request, "core/signup.html", context)


def logout_page(request):
    logout(request)
    return redirect("login_page")
