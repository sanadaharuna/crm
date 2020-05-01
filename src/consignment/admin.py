from django.contrib import admin
from .models import Consignment


@admin.register(Consignment)
class ConsignmentAdmin(admin.ModelAdmin):
    pass
