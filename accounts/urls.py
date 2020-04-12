from django.contrib import admin
from django.urls import path
from .views import home, products, customer, create_order

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk_test>/', customer, name='customer'),
    path('create_order/', create_order, name='create_order'),
]
