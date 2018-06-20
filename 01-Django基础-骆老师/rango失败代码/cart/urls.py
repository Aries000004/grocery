from django.urls import path

from cart import views

urlpatterns = [
    path('', views.index, name='cart_index'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name='show_cart'),
    path('clear_cart', views.clear_cart, name='clear_cart')
]