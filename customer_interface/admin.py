from django.contrib import admin
from .models import Cust_login, Cust_detail, Cust_addres, Cust_lift, Cust_purchase, Cust_subscription

admin.site.register(Cust_login)
admin.site.register(Cust_detail)
admin.site.register(Cust_addres)
admin.site.register(Cust_lift)
admin.site.register(Cust_purchase)
admin.site.register(Cust_subscription)
