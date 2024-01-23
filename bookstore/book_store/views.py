from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Book Store',
        'content': 'Книжный магазин - BOOK STORE',
    }
    return render(request, 'bookstore/index.html', context)


def about(request):
    context = {
        'title': 'Book Store - О сайте',
        'content': 'Информация о сайте BOOK STORE',
    }
    return render(request, 'bookstore/about.html', context)


def catalog(request):
    return render(request, 'bookstore/catalog.html')


def catalog_by_slug(request, slug):
    return HttpResponse(f"<h1>Каталог: {slug}</h1>")


def cart(request):
    return render(request, 'bookstore/cart.html')
