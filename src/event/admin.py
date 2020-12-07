from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Attendee, Event


class EventResource(resources.ModelResource):
    class Meta:
        model = Event


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
    list_display = ("title", "venue", "kaisaibi", "nendo",)
    ordering = ("-kaisaibi",)


class AttendeeResource(resources.ModelResource):
    class Meta:
        model = Attendee


@admin.register(Attendee)
class AttendeeAdmin(ImportExportModelAdmin):
    resource_class = AttendeeResource
    list_display = ("eradcode", "shimei", "shozoku", )
    list_select_related = ("event", )
    search_fields = ("event",)
