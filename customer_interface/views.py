from django.shortcuts import render
from customer_interface import models
from .forms import SignupUser, LoginUser

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
    form = SignupUser()
    if request.method == 'GET':
        return render(request, "customer_interface/signup.html",{'form':form})
    else:
        if request.POST['Password'] == request.POST['Password_Again']:
            form = SignupUser(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return home(request)
            else:
                print("Error Form Invalid")

    #return render(request, "customer_interface/signup.html",{'form':form}
