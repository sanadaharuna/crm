from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Station, Member


class StationResource(resources.ModelResource):
    class Meta:
        model = Station


@admin.register(Station)
class EventAdmin(ImportExportModelAdmin):
    resource_class = StationResource
    list_display = ("attached_to", "name", "date_of_establishment")
    ordering = ("attached_to", "name")


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ("eradcode", "shimei", "shozoku", )
    list_select_related = ("station", )
    search_fields = ("station",)
