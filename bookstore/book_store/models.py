from django.db import models
from django.urls import reverse
from goods.models import Item


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    photo = models.ImageField(
        upload_to='photos/users/Y%/m%/d%',
        verbose_name='Фото',
        default='photos/default/default.jpg',
        blank=True
    )
    email = models.EmailField(verbose_name='Электронная почта')
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('users', kwargs={'users_id': self.pk})

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'


class Cart(models.Model):
    id_customer = models.OneToOneField(
        'Users',
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    items = models.ManyToManyField(
        Item,
        related_name="cart",
        blank=True,
        verbose_name='Покупки'
    )
    count = models.IntegerField()


class History(models.Model):
    id_customer = models.OneToOneField(
        'Users',
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    items = models.ManyToManyField(
        Item,
        related_name='histories',
        blank=True,
        verbose_name='Покупки'
    )
    count = models.IntegerField(verbose_name='Количество')


