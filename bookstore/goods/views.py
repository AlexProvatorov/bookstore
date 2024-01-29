from django.shortcuts import render

from book_store.models import Tags, Items


# Create your views here.
def catalog(request):

    tags = Tags.objects.filter(tags='tags')

    context = {
        'title': 'Book Store - Каталог',
        'tags': tags,
    }

    return render(request, 'goods/catalog.html', context)


def product(request):

    items = Items.objects.all()

    context = {
        'title': 'Book Store - Товары',
        'items': items,
    }

    return render(request, 'goods/product.html', context)
