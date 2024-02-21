from django.shortcuts import render, redirect
from carts.models import Cart
from goods.models import Item
from django.shortcuts import get_object_or_404


def view_cart(request):
    """
    Представление для отображения товаров в корзине.
    """
    cart_positions = Cart.objects.filter(
        id_customer=request.user.id).order_by("id_item_id")
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

    if not created and cart_position.count < cart_position.id_item.count_in_stock:
        cart_position.count += 1
        cart_position.save()

    return redirect(request.META['HTTP_REFERER'])


def remove_cart(request, item_id):

    item_id = get_object_or_404(Item, pk=item_id)

    cart_position, deleted = Cart.objects.get_or_create(
        id_customer=request.user,
        id_item=item_id,
    )

    if not deleted and cart_position.count > 1:
        cart_position.count -= 1
        cart_position.save()

    return redirect(request.META['HTTP_REFERER'])


def remove_cart_position(request, item_id):

    item_id = get_object_or_404(Item, pk=item_id)

    cart_position, deleted = Cart.objects.get_or_create(
        id_customer=request.user,
        id_item=item_id,
    )

    cart_position.delete()

    return redirect(request.META['HTTP_REFERER'])
