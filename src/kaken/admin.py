from django.contrib import admin
from .models import Kaken, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Kaken)
class KakenAdmin(admin.ModelAdmin):
    pass
