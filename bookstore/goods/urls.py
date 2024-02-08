from django.urls import path

from . import views

urlpatterns = [
    path('', views.item, name='catalog'),
    path('product/<int:product_id>/', views.item_in_detail, name='product'),
]
