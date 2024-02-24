from django.db import models
from users.models import User
from goods.models import Item
from django.db.models import Q


class Cart(models.Model):
    CHOICES = (
        ('COMPLETED', 'Завершен'),
        ('PENDING', 'В процессе'),
        ('CANCELLED', 'Отменен'),
    )

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
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    status = models.CharField(
        max_length=255,
        choices=CHOICES,
        verbose_name='Статус'
    )

    def __str__(self):
        return (f"Корзина {self.id_customer} | Товар {self.id_item.name}"
                f" | Количество {self.count} | Цена {self.id_item.cost}"
                f" | Сумма {self.id_item.cost * self.count}"
                f" | Статус {self.status}")

    class Meta:
        db_table = 'carts_carts'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    class CartManager(models.Manager):
        """
        Кастомный менеджер для модели корзины.
        """

        def all(self):
            return self.get_queryset().filter(Q(status='CANCELLED') | Q(status='PENDING') | Q(status=''))

    cart_objects = CartManager()
