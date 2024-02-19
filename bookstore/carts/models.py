from django.db import models
from users.models import User
from goods.models import Item


class Cart(models.Model):
    id_customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    id_item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="cart",
        blank=True,
        verbose_name='Товар',
    )
    count = models.PositiveIntegerField(default=1)
    pay_confirmed = models.BooleanField(default=False, verbose_name='Оплата подтверждена')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина {self.id_customer} | Товар {self.id_item.name} | Количество {self.count}"

    class Meta:
        db_table = 'carts_carts'


class History(models.Model):
    id_customer = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    items = models.ManyToManyField(
        Item,
        related_name='history',
        blank=True,
        verbose_name='История покупок'
    )
    count = models.IntegerField(verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carts_histories'

