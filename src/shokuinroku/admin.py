from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Shokuin


@admin.register(Shokuin)
class ShokuinAdmin(ImportExportModelAdmin):
    ordering = ["kijunbi", "shokuin_id"]


class ShokuinResource(resources.ModelResource):
    class Meta:
        model = Shokuin
