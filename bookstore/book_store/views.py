from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from book_store.models import Items


def index(request):

    items = Items.objects.all()
    paginator = Paginator(items, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Book Store',
        'content': 'Книжный магазин - BOOK STORE',
        'items': items,
        'page_obj': page_obj,
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
