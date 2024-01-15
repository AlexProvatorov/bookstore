from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения BookStore")


def catalog(request):
    return HttpResponse("<h1>Каталог</h1>")
