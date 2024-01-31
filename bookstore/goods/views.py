from django.shortcuts import render

from book_store.models import Tags, Items, Authors


# Create your views here.
def catalog(request):

    tags = Tags.objects.all()
    items = Items.objects.all()

    context = {
        'title': 'Book Store - Каталог',
        'tags': tags,
        'items': items,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_id):

    item = Items.objects.get(pk=product_id)
    authors = Authors.objects.filter(books__exact=item)
    tags = Tags.objects.filter(item__exact=item)

    context = {
        'title': 'Book Store - Товары',
        'item': item,
        'authors': ', '.join(author.full_name for author in authors),
        'tags': ', '.join(tage.name for tage in tags),
    }

    return render(request, 'goods/product.html', context)
