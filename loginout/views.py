from django.shortcuts import render, redirect
from loginout.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def mylogin(request):
    context = {"title": "Login Page"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Account not exist Please create one!!")
            return redirect("register")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("login")
        else:
            login(request, user)
            return redirect('home')

    return render(request, "login.html", context=context)


def register(request):
    context = {"title": "Register Page"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Account already created")
            return redirect("login")
        else:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            messages.info(request, "Account created successfully")
            return redirect("login")
    return render(request, "register.html", context=context)

@login_required(login_url='login')
def home(request):
    context = {"title": "Home Page"}
    return render(request, "home.html", context)

@login_required(login_url='login')
def mylogout(request):
    logout(request)
    return redirect('login')
