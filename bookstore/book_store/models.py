from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()
    count_in_stock = models.IntegerField()
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags')
    id_cart = models.ForeignKey(
        'Cart',
        on_delete=models.PROTECT,
    )


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    items = models.ManyToManyField('Items', blank=True, related_name='items')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'


class Cart(models.Model):
    id_customer = models.OneToOneField(
        'Customers',
        on_delete=models.PROTECT,
    )
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


# поле тайп в итемс под удаление
# id cart при создании фигурки и книги вфт
# при создании юзера ему предлагают добавить итем, а не книгу или фигурку
