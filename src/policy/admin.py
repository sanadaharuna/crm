from django.contrib import admin

from .models import Policy, Participant


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
