"""liftservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer_interface import views
from Admin_panel import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('login/', include('customer_interface.urls')),
    #path('signup/', include('customer_interface.urls')),
    path('customer_interface/', include('customer_interface.urls')),
    path('Admin_panel/', include('Admin_panel.urls')),
    path('Work_force/', include('Work_force.urls')),





]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
