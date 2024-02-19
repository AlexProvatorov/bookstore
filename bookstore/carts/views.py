from django.shortcuts import render, redirect
from carts.models import Cart
from goods.models import Item
from django.shortcuts import get_object_or_404


def view_cart(request):
    cart_positions = Cart.objects.all()
    context = {
        'title': 'Корзина',
        'content': 'Корзина',
        'cart_positions': cart_positions,
    }
    return render(request, 'carts/view_cart.html', context)


def add_cart(request, item_id):

    if not request.user.is_authenticated:
        return redirect('login')

    item_id = get_object_or_404(Item, pk=item_id)

    cart_position, created = Cart.objects.get_or_create(
        id_customer=request.user,
        id_item=item_id,
    )

    if not created:
        cart_position.count += 1
        cart_position.save()

    return redirect(request.META['HTTP_REFERER'])


def change_cart(request, item_id):
    return render(request, 'carts/change_cart.html')


def remove_cart(request, item_id):
    return render(request, 'carts/remove_cart.html')
