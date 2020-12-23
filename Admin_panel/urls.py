from django.urls import path
from . import views

app_name = 'Admin_panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('user/', views.userpage, name='userpage'),
    path('details/', views.details, name='details'),

]
