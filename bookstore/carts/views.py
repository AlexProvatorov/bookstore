from django.shortcuts import render, redirect
from carts.models import Cart
from goods.models import Item


def view_cart(request):
    cart_list = Cart.objects.all()
    context = {
        'title': 'Корзина',
        'content': 'Корзина',
        'cart_list': cart_list,
    }
    return render(request, 'carts/view_cart.html', context)


def add_cart(request, item_id):
    cart_item = Item.objects.get(id=item_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, items=cart_item)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.count += 1
                cart.save()

        else:
            Cart.objects.create(user=request.user, cart_item=cart_item, count=1)

    return redirect(request.META['HTTP_REFERER'])


def change_cart(request, item_id):
    return render(request, 'carts/change_cart.html')


def remove_cart(request, item_id):
    return render(request, 'carts/remove_cart.html')
