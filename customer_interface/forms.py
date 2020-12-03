from django import forms
from .models import Cust_login, Cust_detail, Cust_addres

class LoginUser(forms.ModelForm):
    login_Username = forms.EmailField(widget=forms.EmailInput)
    login_Password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Cust_login
        fields = ['login_Username','login_Password']


class SignupUser(forms.ModelForm):
    Firstname = forms.CharField(widget=forms.TextInput)
    Lastname = forms.CharField(widget=forms.TextInput)
    signup_Username = forms.EmailField(widget=forms.EmailInput)
    signup_Password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Cust_detail
        fields = ['Firstname','Lastname','signup_Username','signup_Password']


class Cust_address_details(forms.ModelForm):
    class Meta():
        model = Cust_addres
        fields = ['Phone_no','house_no','building_name','street','area','city','state','pincode']
