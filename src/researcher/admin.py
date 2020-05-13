from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Researcher


@admin.register(Researcher)
class ResearcherAdmin(ImportExportModelAdmin):
    ordering = ["kijunbi", "researcher_id"]


class ResearcherResource(resources.ModelResource):
    class Meta:
        model = Researcher
