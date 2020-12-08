from django.db import models
from django.contrib.auth.models import User


class Cust_addres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_no = models.CharField(max_length=20)
    house_no = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)

"""
    def __str__(self):
        return self.user
"""

class Cust_lift(models.Model):
    #cust_id = models.CharField(max_length=10,blank=True)
    count = models.CharField(max_length=3,blank=True)
    lift_id = models.CharField(max_length=10,blank=True)
    type = models.CharField(max_length=1,blank=True)

    def __str__(self):
        return self.title


class Cust_purchase(models.Model):
    #cust_id = models.CharField(max_length=10,blank=True)
    invoice = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.title


class Cust_subscription(models.Model):
    #cust_id = models.CharField(max_length=10,blank=True)
    subscription_id = models.CharField(max_length=15,blank=True)
    subscription_type = models.CharField(max_length=1,blank=True)
    valid_from = models.DateField(auto_now_add=True,blank=True)
    valid_to = models.DateField(auto_now_add=False,blank=True)
    invoice_no = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    image = models.ImageField(upload_to='customer_interface/images')
