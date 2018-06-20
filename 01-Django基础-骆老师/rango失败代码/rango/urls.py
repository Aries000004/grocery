from django.urls import path

from rango import views as rg_views

urlpatterns = [
    path('', rg_views.index, name='rango_index'),
]