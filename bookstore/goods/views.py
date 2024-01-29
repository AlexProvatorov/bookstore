from django.shortcuts import render

from book_store.models import Tags


# Create your views here.
def catalog(request):

    tags = Tags.objects.all()

    context = {
        'title': 'Book Store - Каталог',
        'tags': tags,
    }

    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
