from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='website-home'),
    path('register', views.register, name='hey'),
    path('login',views.login,name="login"),
    path('error',views.error,name='error'),
    ]
