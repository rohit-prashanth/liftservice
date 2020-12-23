from django import forms
from .models import Admin_addres


class Admin_address_details(forms.ModelForm):
    class Meta():
        model = Admin_addres
        fields = ['Phone_no','house_no','building_name','street','area','city','state','pincode']
