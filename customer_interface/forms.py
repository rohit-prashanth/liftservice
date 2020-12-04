from django import forms
from .models import Cust_detail, Cust_addres


class cust_login(forms.Form):
    Username = forms.CharField()
    Firstname = forms.CharField()
    Lastname = forms.CharField()
    Email_adress = forms.EmailField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    Password_Again = forms.CharField(widget=forms.PasswordInput)


class Cust_address_details(forms.ModelForm):
    class Meta():
        model = Cust_addres
        fields = ['Phone_no','house_no','building_name','street','area','city','state','pincode']
