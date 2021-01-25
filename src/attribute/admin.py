from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Attribute, Eligible


class AttributeResource(resources.ModelResource):
    class Meta:
        model = Attribute


@admin.register(Attribute)
class AttributeAdmin(ImportExportModelAdmin):
    resource_class = AttributeResource
    list_display = ("zokusei",)
    search_fields = ("zokusei",)
    ordering = ("id",)


class EligibleResource(resources.ModelResource):
    class Meta:
        model = Eligible


@admin.register(Eligible)
class EligibleAdmin(ImportExportModelAdmin):
    resource_class = EligibleResource
    list_select_related = ("attribute", )
    list_display = ("nendo", "format_attribute_zokusei", "eradcode",
                    "shimei", "shozoku", "bikou")

    def format_attribute_zokusei(self, obj):
        if obj.attribute is not None:
            return obj.attribute.zokusei

    format_attribute_zokusei.short_description = "属性"
    format_attribute_zokusei.admin_order_field = "attribute__zokusei"
