from django import forms
from .models import Cust_addres


class Cust_address_details(forms.ModelForm):
    class Meta():
        model = Cust_addres
        fields = ['Phone_no','house_no','building_name','street','area','city','state','pincode']
