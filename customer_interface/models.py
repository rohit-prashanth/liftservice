from django.db import models

class Cust_login(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=15)
    Cust_id = models.CharField(max_length=10)

    def __str__(self):
        return self.Username

class Cust_detail(models.Model):
    Cust_id = models.CharField(max_length=10,blank=True)
    Firstname = models.CharField(max_length=30,blank=True)
    Lastname = models.CharField(max_length=30,blank=True)
    Username = models.EmailField(max_length=40,blank=True)
    Password = models.CharField(max_length=15,blank=True)
    Password_Again = models.CharField(max_length=15,blank=True)
    Address = models.CharField(max_length=100,blank=True)
    Address_2 = models.CharField(max_length=100,blank=True)
    Phone_no = models.CharField(max_length=10,blank=True)
    City = models.CharField(max_length=15,blank=True)
    State = models.CharField(max_length=15,blank=True)
    Zip =  models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.Firstname


class Cust_addres(models.Model):
    cust_id = models.CharField(max_length=10)
    house_no = models.CharField(max_length=50)
    building_name = models.CharField(max_length=50)
    street = models.CharField(max_length=60)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.title


class Cust_lift(models.Model):
    cust_id = models.CharField(max_length=10)
    count = models.CharField(max_length=3)
    lift_id = models.CharField(max_length=10)
    type = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Cust_purchase(models.Model):
    cust_id = models.CharField(max_length=10)
    invoice = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Cust_subscription(models.Model):
    cust_id = models.CharField(max_length=10)
    subscription_id = models.CharField(max_length=15)
    subscription_type = models.CharField(max_length=1)
    valid_from = models.DateField(auto_now_add=True)
    valid_to = models.DateField(auto_now_add=False)
    invoice_no = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Media(models.Model):
    image = models.ImageField(upload_to='customer_interface/images')
