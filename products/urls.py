from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("", views.index, name="Products"),
    path("trending/", views.trending, name="Trending"),
    path("new/", views.new, name="New"),
    path("contact/", views.contact, name="Contact"),
    path("products/", views.products, name="Products"),
    path("purchase/", views.purchase, name="Purchase"),
    path("products/leds/", views.leds, name="LED"),
    path("products/mobiles/",views.mobiles,name='Mobile'),
    path("products/laptops/",views.laptops,name="Laptop"),


]
