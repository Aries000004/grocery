
from django.conf.urls import url

from car_no import views

urlpatterns = [
    url('car', views.car, name='car'),
    url('query', views.query, name='query')
]
