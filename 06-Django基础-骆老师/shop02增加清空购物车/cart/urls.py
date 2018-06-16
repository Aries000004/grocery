from django.contrib import admin
from django.urls import path, include

from cart import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name='show_cart'),
]