from django.shortcuts import render

def home(request):
    return render(request, "customer_interface/home.html")

def login(request):
    return render(request, "customer_interface/login.html")

def signup(request):
    return render(request, "customer_interface/signup.html")
