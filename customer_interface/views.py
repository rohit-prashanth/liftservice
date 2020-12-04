from django.shortcuts import render, redirect, get_object_or_404
from customer_interface import models
from .forms import  Cust_address_details, cust_login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse

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
                login(request, user)
                return redirect('customer_interface:details')
            except IntegrityError:
                return render(request, 'customer_interface/signup.html',{"error":"This username has already been taken, Please choose a unique username."})
        else:
            return render(request, 'customer_interface/signup.html',{'error': 'Passwords did not match'})


def user(request):
    return render(request, "customer_interface/user.html")


def details(request):
    if request.method == 'GET':
        return render(request,'customer_interface/details.html')
    else:
        form= Cust_address_details(request.POST)
        if form.is_valid():
            form.Phone_no = request.POST.get('Phone_no')
            form.house_no = request.POST.get('house_no')
            form.building_name = request.POST.get('building_name')
            form.street = request.POST.get('street')
            form.area = request.POST.get('area')
            form.city  = request.POST.get('city')
            form.state = request.POST.get('state')
            form.pincode = request.POST.get('pincode')
            form.save()
            return redirect('customer_interface:welcome')

def welcome(request):
    return render(request,'customer_interface/welcome.html')
