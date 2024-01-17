from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()
    count_in_stock = models.IntegerField()
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags')


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    # items = models.ManyToManyField('Items', blank=True, related_name='items')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'


class Cart(models.Model):
    id_customer = models.OneToOneField(
        'Users',
        on_delete=models.PROTECT,
    )
    items = models.ManyToManyField('Items', blank=True)
    count = models.IntegerField()


class History(models.Model):
    id_customer = models.OneToOneField(
        'Users',
        on_delete=models.PROTECT,
    )
    items = models.ManyToManyField('Items', blank=True)
    count = models.IntegerField()


class Books(Items):
    authors = models.ManyToManyField('Authors', related_name='authors')
    date_release = models.DateField()

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'


class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Автор'


class Figurine(Items):
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()

    class Meta:
        verbose_name = 'Фигурки'
        verbose_name_plural = 'Фигурка'

