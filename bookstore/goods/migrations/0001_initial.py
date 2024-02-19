# Generated by Django 5.0.1 on 2024-02-19 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Авторы',
                'verbose_name_plural': 'Автор',
                'db_table': 'items_authors',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('count_in_stock', models.IntegerField(verbose_name='Количество в наличии')),
                ('photo', models.ImageField(blank=True, default='photos/default/default.jpg', upload_to='photos/items/Y%/m%/d%', verbose_name='Фото')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Время последнего редактирования')),
            ],
            options={
                'db_table': 'items_items',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Имя тега')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Тег',
                'db_table': 'items_tags',
            },
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.item')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('height', models.FloatField(verbose_name='Высота')),
                ('width', models.FloatField(verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'Фигурки',
                'verbose_name_plural': 'Фигурка',
                'db_table': 'items_figurines',
            },
            bases=('goods.item',),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='item', to='goods.tag', verbose_name='Теги'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.item')),
                ('date_release', models.DateField(verbose_name='Дата выхода')),
                ('authors', models.ManyToManyField(related_name='book', to='goods.author', verbose_name='Авторы')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книга',
                'db_table': 'items_books',
            },
            bases=('goods.item',),
        ),
    ]
