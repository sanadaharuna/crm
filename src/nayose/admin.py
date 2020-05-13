from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Nayose


@admin.register(Nayose)
class NayoseAdmin(ImportExportModelAdmin):
    ordering = ["nayose_id"]


class NayoseResource(resources.ModelResource):
    class Meta:
        model = Nayose
