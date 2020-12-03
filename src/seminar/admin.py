from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Attendee, Lecturer, Seminar


class SeminarResource(resources.ModelResource):
    class Meta:
        model = Seminar


@admin.register(Seminar)
class SeminarAdmin(ImportExportModelAdmin):
    resource_class = SeminarResource
    list_display = ("title", "venue", "kaisaibi", "nendo",)
    ordering = ("-kaisaibi",)


class AttendeeResource(resources.ModelResource):
    class Meta:
        model = Attendee


@admin.register(Attendee)
class AttendeeAdmin(ImportExportModelAdmin):
    resource_class = AttendeeResource
    list_display = ("eradcode", "shimei", "shozoku", "seminar")
    list_select_related = ("seminar", )
    search_fields = ("seminar",)


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    pass
