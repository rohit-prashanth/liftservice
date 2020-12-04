from django.urls import path
from . import views

app_name = 'customer_interface'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('user/', views.user, name='user'),

]
