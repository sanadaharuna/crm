from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Member, Project


#
# 課題データ
#
class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ("id", "nendo", "kubun", "saihi", "kadaimei")


#
# 応募者データ
#
class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ("project", "role", "shimei", "shozoku")
