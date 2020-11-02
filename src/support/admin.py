from django.contrib import admin
from .models import Kakenhi, CompetitiveFund, Matching
from import_export import resources
from import_export.admin import ImportExportModelAdmin


#
# Kakenhi
#

class KakenhiResource(resources.ModelResource):
    class Meta:
        model = Kakenhi


@admin.register(Kakenhi)
class KakenhiAdmin(ImportExportModelAdmin):
    resource_class = KakenhiResource
    list_display = ("pk", "nendo", "uketsukebi", "eradcode", "shimei", "shozoku",
                    "shutantou", "fukutantou", "shumoku", "kanryoubi", "saihi")


#
# Matching
#

class CompetitivefundResource(resources.ModelResource):
    class Meta:
        model = CompetitiveFund


@admin.register(CompetitiveFund)
class CompetitiveFundAdmin(ImportExportModelAdmin):
    resource_class = CompetitivefundResource
    list_display = ("pk", "nendo", "uketsukebi", "eradcode", "shimei", "shozoku",
                    "shutantou", "fukutantou", "haibunkikan", "koubomei", "kanryoubi", "saihi")


#
# Matching
#


class MatchingResource(resources.ModelResource):
    class Meta:
        model = Matching


@admin.register(Matching)
class MatchingAdmin(ImportExportModelAdmin):
    resource_class = MatchingResource
    list_display = ("pk", "nendo", "uketsukebi", "eradcode",
                    "shimei", "shozoku", "shutantou", "fukutantou", "kanryoubi")
