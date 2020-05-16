from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from nayose.models import Nayose, Researcher, Shokuin


@admin.register(Nayose)
class NayoseAdmin(ImportExportModelAdmin):
    ordering = ["nayose_id"]


class NayoseResource(resources.ModelResource):
    class Meta:
        model = Nayose


@admin.register(Shokuin)
class ShokuinAdmin(ImportExportModelAdmin):
    ordering = ["kijunbi", "shokuin_id"]


class ShokuinResource(resources.ModelResource):
    class Meta:
        model = Shokuin


@admin.register(Researcher)
class ResearcherAdmin(ImportExportModelAdmin):
    ordering = ["kijunbi", "researcher_id"]


class ResearcherResource(resources.ModelResource):
    class Meta:
        model = Researcher
