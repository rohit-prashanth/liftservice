from django.shortcuts import render, redirect, get_object_or_404,reverse
from Admin_panel import models
from .forms import  Admin_address_details
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    return render(request, "Admin_panel/home.html")

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'Admin_panel/login.html')
    else:
        user = authenticate(request, username=request.POST['username'] , password=request.POST['password'])
        if user is None:
            return render(request, 'Admin_panel/login.html', {'error':'Username and Password does not exist'})
        else:
            login(request,user)
            return redirect("Admin_panel:userpage")

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect("Admin_panel:home")


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'Admin_panel/signup.html')
    else:
        if request.POST['Password'] == request.POST['Password_Again']:
            try:
                user = User.objects.create_user(request.POST['Username'],password=request.POST['Password'],first_name=request.POST['Firstname'],last_name=request.POST['Lastname'],email=request.POST['Email'])
                user.save()
                login(request, user)
                return redirect('Admin_panel:details')
            except IntegrityError:
                return render(request, 'Admin_panel/signup.html',{"error":"This username has already been taken, Please choose a unique username."})
        else:
            return render(request, 'Admin_panel/signup.html',{'error': 'Passwords did not match'})


def userpage(request):
    return render(request, "Admin_panel/userpage.html")


def details(request):
    if request.method == 'GET':
        return render(request,"Admin_panel/details.html")
    else:
        try:
            form = Admin_address_details(request.POST)
            form.Phone_no = request.POST.get('Phone_no')
            form.house_no = request.POST.get('house_no')
            form.building_name = request.POST.get('building_name')
            form.street = request.POST.get('street')
            form.area = request.POST.get('area')
            form.city  = request.POST.get('city')
            form.state = request.POST.get('state')
            form.pincode = request.POST.get('pincode')
            #user_form = form.save(commit = False)
            #form.username = request.POST.get('user')
            newuser = form.save(commit = False)
            newuser.user = request.user
            newuser.save()
            return redirect('Admin_panel:userpage')
        except ValueError:
            return render(request,"Admin_panel/details.html",{'error':'bad data entered'})
