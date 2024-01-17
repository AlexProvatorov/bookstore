from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'bookstore/index.html')


def catalog(request):
    return render(request, 'bookstore/catalog.html')


def catalog_by_slug(request, slug):
    return HttpResponse(f"<h1>Каталог: {slug}</h1>")


def cart(request):
    return render(request, 'bookstore/cart.html')
