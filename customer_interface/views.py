from django.shortcuts import render, redirect, get_object_or_404
from customer_interface import models
from .forms import  Cust_address_details, cust_login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


def home(request):
    return render(request, "customer_interface/home.html")

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'customer_interface/login.html')
    else:
        user = authenticate(request, username=request.POST['username'] , password=request.POST['password'])
        if user is None:
            return render(request, 'customer_interface/login.html', {'error':'Username and Password does not exist'})
        else:
            login(request,user)
            return render(request, "customer_interface/user.html")

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, "customer_interface/user.html")


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'customer_interface/signup.html')
    else:
        if request.POST['Password'] == request.POST['Password_Again']:
            try:
                user = User.objects.create_user(request.POST['Username'],password=request.POST['Password'],first_name=request.POST['Firstname'],last_name=request.POST['Lastname'],email=request.POST['Email'])
                user.save()
                return render(request, 'customer_interface/login.html')
            except IntegrityError:
                return render(request, 'customer_interface/signup.html',{"error":"This username has already been taken, Please choose a unique username."})
        else:
            return render(request, 'customer_interface/signup.html',{'error': 'Passwords did not match'})


def user(request):
    return render(request, "customer_interface/user.html")
