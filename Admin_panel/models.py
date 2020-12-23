from django.db import models
from django.contrib.auth.models import User


class Admin_addres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_no = models.CharField(max_length=20)
    house_no = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)


    def __str__(self):
        return self.user.username



class Media(models.Model):
    image = models.ImageField(upload_to='Admin_panel/images')
