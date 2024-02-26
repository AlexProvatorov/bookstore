from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_cart/<int:item_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_position/<int:item_id>/', views.remove_cart_position,
         name='remove_cart_position'),
    path('create_order/', views.create_order, name='create_order'),
]
