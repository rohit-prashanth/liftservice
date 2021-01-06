from django import forms
from .models import Work_force_addres


class Work_force_address_details(forms.ModelForm):
    class Meta():
        model = Work_force_addres
        fields = ['Phone_no','house_no','building_name','street','area','city','state','pincode']
