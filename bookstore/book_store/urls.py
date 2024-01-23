from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>', views.catalog_by_slug),
    path('cart/', views.cart, name='cart'),
]
