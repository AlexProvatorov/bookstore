from django.db import models
from django.urls import reverse


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cost = models.IntegerField(verbose_name='Цена')
    count_in_stock = models.IntegerField(verbose_name='Количество в наличии')
    tags = models.ManyToManyField(
        'Tags',
        blank=True,
        related_name='tags',
        verbose_name='Теги'
    )
    photo = models.ImageField(
        upload_to='photos/items/Y%/m%/d%',
        default='photos/default/default.jpg',
        blank=True,
        verbose_name='Фото'
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    time_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего редактирования'
    )

    def __str__(self):
        return self.name


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Имя тега')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'


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
        'Items',
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
        'Items',
        blank=True,
        verbose_name='Покупки'
    )
    count = models.IntegerField(verbose_name='Количество')


class Books(Items):
    authors = models.ManyToManyField(
        'Authors',
        related_name='authors',
        verbose_name='Авторы',
    )
    date_release = models.DateField(verbose_name='Дата выхода')

    def get_absolute_url(self):
        return reverse('books', kwargs={'books_id': self.pk})

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'


class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('authors', kwargs={'authors_id': self.pk})

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Автор'


class Figurine(Items):
    weight = models.FloatField(verbose_name='Вес')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')

    def get_absolute_url(self):
        return reverse('figurine', kwargs={'figurine_id': self.pk})

    class Meta:
        verbose_name = 'Фигурки'
        verbose_name_plural = 'Фигурка'
