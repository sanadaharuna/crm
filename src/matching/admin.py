from django.contrib import admin

from .models import Matching


@admin.register(Matching)
class MatchingAdmin(admin.ModelAdmin):
    pass
