from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('Products',views.Products, name='Products'),
    path('login',views.login, name='Login')
]
