from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from nayose.models import Nayose


class NayoseReseource(resources.ModelResource):
    class Meta:
        model = Nayose


@admin.register(Nayose)
class NayoseAdmin(ImportExportModelAdmin):
    resource_class = NayoseReseource
    list_display = ("nayose_id", "eradcode", "shokuincode", "hijoukincode",
                    "kanjishimei_sei", "kanjishimei_mei", "kanashimei_sei", "kanashimei_mei",
                    "seinengappi", "seibetsu", "orcid")
