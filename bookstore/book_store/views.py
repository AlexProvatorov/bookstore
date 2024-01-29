from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from book_store.models import Items


def index(request):

    items = Items.objects.all()

    context = {
        'title': 'Book Store',
        'content': 'Книжный магазин - BOOK STORE',
        'items': items,
    }
    return render(request, 'book_store/index.html', context=context)


def about(request):
    context = {
        'title': 'Book Store - О сайте',
        'content': 'Информация о сайте BOOK STORE',
    }
    return render(request, 'book_store/about.html', context)


def cart(request):
    return render(request, 'book_store/cart.html')
