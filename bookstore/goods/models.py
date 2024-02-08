from django.db import models
from django.urls import reverse


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cost = models.IntegerField(verbose_name='Цена')
    count_in_stock = models.IntegerField(verbose_name='Количество в наличии')
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='item',
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

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        db_table = 'items_items'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Имя тега')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'
        db_table = 'items_tags'


class Book(Item):
    authors = models.ManyToManyField(
        'Author',
        related_name='book',
        verbose_name='Авторы',
    )
    date_release = models.DateField(verbose_name='Дата выхода')

    def get_absolute_url(self):
        return reverse('books', kwargs={'books_id': self.pk})

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'
        db_table = 'items_books'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('authors', kwargs={'authors_id': self.pk})

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Автор'
        db_table = 'items_authors'


class Figure(Item):
    weight = models.FloatField(verbose_name='Вес')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')

    def get_absolute_url(self):
        return reverse('figurine', kwargs={'figurine_id': self.pk})

    class Meta:
        verbose_name = 'Фигурки'
        verbose_name_plural = 'Фигурка'
        db_table = 'items_figurines'

