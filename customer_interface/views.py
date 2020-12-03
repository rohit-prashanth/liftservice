from django.shortcuts import render, redirect, get_object_or_404
from customer_interface import models
from .forms import SignupUser, LoginUser, Cust_address_details
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, "customer_interface/home.html")

def login(request):
    form = LoginUser()
    if request.method == 'GET':
        return render(request, 'customer_interface/login.html',{'form':form})
    else:
        user = authenticate(request, username=request.POST['Username'] , password=request.POST['Password'])
        if user is None:
            return render(request, 'customer_interface/login.html', {'form':form, 'error':'Username and Password does not exist'})
        else:
            login(request,user)
            return home(request)

def signup(request):
    cust_login_user = LoginUser(request.POST)
    cust_detail_user = SignupUser(request.POST)
    cust_address_user = Cust_address_details(request.POST)
    if request.method == 'GET':
        return render(request, "customer_interface/signup.html")
    else:
        if request.POST['Password'] == request.POST['Password_Again']:

            if cust_login_user.is_valid():
                #Cust_login table
                cust_login_user.login_Username = request.POST.get('Username')
                cust_login_user.login_Password = request.POST.get('Password')
                cust_login_user.save()

            elif cust_detail_user.is_valid():
                #Cust_detail table
                cust_detail_user.Firstname = request.POST.get('Firstname')
                cust_detail_user.Lastname = request.POST.get('Lastname')
                cust_detail_user.signup_Username = request.POST.get('Username')
                cust_detail_user.signup_Password = request.POST.get('Password')
                cust_detail_user.save()

            elif cust_address_user.is_valid():
                #Cust_addres table
                cust_address_user.Phone_no = request.POST.get('Phone_no')
                cust_address_user.house_no = request.POST.get('house_no')
                cust_address_user.building_name = request.POST.get('building_name')
                cust_address_user.street = request.POST.get('street')
                cust_address_user.area = request.POST.get('area')
                cust_address_user.city = request.POST.get('City')
                cust_address_user.state = request.POST.get('State')
                cust_address_user.pincode = request.POST.get('Zip')
                cust_address_user.save()

            else:
                return render(request, "customer_interface/signup.html",{'error':'enter unique username or fill all the fields'})



            result = cust_detail_user.cleaned_data.get('Firstname')
            return render(request, "customer_interface/user.html",{'result':result})
        else:
            return render(request, "customer_interface/signup.html",{'error':'Username and Password does not exist'})
