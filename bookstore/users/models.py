from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    photo = models.ImageField(
        upload_to='photos/users/Y%/m%/d%',
        verbose_name='Фото',
        default='photos/default/default.jpg',
        blank=True
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        auto_now_add=True
    )

#    def __str__(self):
#       return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'
        db_table = 'users_users'


