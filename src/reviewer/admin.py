from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .adminResources import ReviewerResource
from .models import Reviewer


# @admin.register(Reviewer)
# class ReviewerAdmin(admin.ModelAdmin):
#     pass


@admin.register(Reviewer)
class ReviewerAdmin(ImportExportModelAdmin):
    resource_class = ReviewerResource
