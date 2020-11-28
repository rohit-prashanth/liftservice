from django import forms
from .models import Cust_login, Cust_detail, Cust_addres

class LoginUser(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Cust_login
        fields = ['Username','Password']


class SignupUser(forms.ModelForm):
    Firstname = forms.CharField(widget=forms.TextInput)
    Lastname = forms.CharField(widget=forms.TextInput)
    Username = forms.EmailField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    Password_Again = forms.CharField(widget=forms.PasswordInput)
    Address = forms.CharField(widget=forms.TextInput)
    Address_2 = forms.CharField(widget=forms.TextInput)
    Phone_no = forms.CharField(widget=forms.NumberInput)
    City = forms.CharField(widget=forms.TextInput)
    State = forms.CharField(widget=forms.TextInput)
    Zip =  forms.CharField(widget=forms.NumberInput)

    class Meta():
        model = Cust_detail
        fields = ['Firstname','Lastname','Username','Password','Password_Again','Address','Address_2','Phone_no','City','State','Zip']
