# Generated by Django 5.0.1 on 2024-02-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True, verbose_name='Дата рождения'),
        ),
    ]