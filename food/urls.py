"""
URL configuration for food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',views.home),
    path('DONOR/',views.donor),
    path('ADMIN/',views.admin),
    path('RECIPIENT/',views.recipient),
    path('VOLUNTEER/',views.volunteer),
    path('adddonor/',views.donoradd),
    path('signupadmin/',views.reportshow),
    path('adddetails/',views.fooddetails),
    path('report/',views.showdonor),
    path('foodreport/',views.showfood),
    path('login/',views.login),
    path('user/',views.userprofile),
    


]
