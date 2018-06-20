from django.urls import path

from car_no import views

urlpatterns = [
    path('car', views.car, name='car'),
    path('query', views.query, name='query'),


]