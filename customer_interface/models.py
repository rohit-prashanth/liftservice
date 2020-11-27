from django.db import models

class Cust_login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    cust_id = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Cust_detail(models.Model):
    cust_id = models.CharField(max_length=10)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    username = models.EmailField(max_length=40)

    def __str__(self):
        return self.title


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
