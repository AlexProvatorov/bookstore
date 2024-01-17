from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('catalog/', views.catalog),
    path('catalog/<slug:slug>', views.catalog_by_slug),
    path('cart/', views.cart),
]
