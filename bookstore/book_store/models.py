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


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    items = models.ManyToManyField('Items', blank=True, related_name='items')


class Cart(models.Model):
    id_customer = models.OneToOneField(
        'Customers',
        on_delete=models.PROTECT,
    )
    count = models.IntegerField()


class Books(Items):
    authors = models.ManyToManyField('Authors', related_name='authors')
    date_release = models.DateField()


class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Figurine(Items):
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
