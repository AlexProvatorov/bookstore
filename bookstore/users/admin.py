from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    #fields = ["username"]
    pass
