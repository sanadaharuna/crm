from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

from .models import Member, Project


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
    kubun = fields.Field(attribute="get_kubun_display", column_name="kubun")
    saihi = fields.Field(attribute="get_saihi_display", column_name="saihi")


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ("id", "nendo", "kubun", "saihi", "kadaimei")


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ("role", "shimei", "shozoku", "format_project_kadaimei")
    list_select_related = ("project",)

    def format_project_kadaimei(self, obj):
        if obj.project is not None:
            return obj.project.kadaimei

    format_project_kadaimei.short_description = "課題名"
    format_project_kadaimei.admin_order_field = "project__kadaimei"
