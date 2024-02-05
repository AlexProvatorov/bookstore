from django.shortcuts import render, get_list_or_404

from book_store.models import Tags, Items, Authors


# Create your views here.
def catalog(request, catalog_slug):

    order_by = request.GET.get('order_by', None)
    filter_by_tags = request.GET.get('filter_by_tags', None)
    items = Items.objects.all()

    if catalog_slug == "all":
        items = Items.objects.all()
    else:
        items = get_list_or_404(Items.objects.filter(catalog__slug=catalog_slug))
    if order_by:
        items = items.order_by(order_by)
    if filter_by_tags:
        items = items.filter(tags__name=filter_by_tags)

    tags = Tags.objects.all()

    context = {
        'title': 'Book Store - Каталог',
        'tags': tags,
        'items': items,
        'catalog_slug': catalog_slug,
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
