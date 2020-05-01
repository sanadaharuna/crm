from django.contrib import admin

from .models import Shokuin


@admin.register(Shokuin)
class ShokuinAdmin(admin.ModelAdmin):
    pass

