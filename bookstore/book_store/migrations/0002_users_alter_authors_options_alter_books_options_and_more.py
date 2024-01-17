# Generated by Django 5.0.1 on 2024-01-16 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователь',
            },
        ),
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Авторы', 'verbose_name_plural': 'Автор'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книги', 'verbose_name_plural': 'Книга'},
        ),
        migrations.AlterModelOptions(
            name='figurine',
            options={'verbose_name': 'Фигурки', 'verbose_name_plural': 'Фигурка'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Теги', 'verbose_name_plural': 'Тег'},
        ),
        migrations.RemoveField(
            model_name='items',
            name='id_cart',
        ),
        migrations.RemoveField(
            model_name='items',
            name='type',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='book_store.items'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('items', models.ManyToManyField(blank=True, to='book_store.items')),
                ('id_customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='book_store.users')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='id_customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='book_store.users'),
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]
