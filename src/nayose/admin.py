from django.contrib import admin
from .models import Nayose


@admin.register(Nayose)
class NayoseAdmin(admin.ModelAdmin):
    pass
