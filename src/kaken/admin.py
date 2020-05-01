from django.contrib import admin
from .models import Kaken, Category, SupportType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SupportType)
class SupportTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Kaken)
class KakenAdmin(admin.ModelAdmin):
    pass
