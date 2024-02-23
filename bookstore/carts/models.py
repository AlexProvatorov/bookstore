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
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=255, choices=CHOICES)

    def __str__(self):
        return (f"Корзина {self.id_customer} | Товар {self.id_item.name}"
                f" | Количество {self.count} | Статус {self.status}")

    class Meta:
        db_table = 'carts_carts'

    class CartManager(models.Manager):
        """
        Кастомный менеджер для модели корзины.
        """

        def all(self):
            return self.get_queryset().filter(Q(status='CANCELLED') | Q(status='PENDING') | Q(status=''))

    cart_objects = CartManager()
