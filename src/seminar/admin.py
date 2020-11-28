from django.contrib import admin

from .models import Attendee, Lecturer, Seminar


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    pass
