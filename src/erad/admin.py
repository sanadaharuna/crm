from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Application, Researcher

#
# 研究者データ
#


class ResearcherResource(resources.ModelResource):
    class Meta:
        model = Researcher


@admin.register(Researcher)
class ResearcherAdmin(ImportExportModelAdmin):
    resource_class = ResearcherResource
    list_display = ("eradcode", "kenkyuushashimei_sei",
                    "kenkyuushashimei_mei", "shozoku")


#
# 応募データ
#


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application


@admin.register(Application)
class ApplicationAdmin(ImportExportModelAdmin):
    resource_class = ApplicationResource
    list_display = ("kakushu_no", "nendo", "seidomei",
                    "koubomei", "kadaimei", "eradcode")
