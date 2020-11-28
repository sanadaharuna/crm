from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_title = "Galette CRM"
admin.site.site_header = "Galette CRM"

urlpatterns = [
    path("", include("erad.urls")),
    path("seminar/", include("seminar.urls")),
    path("support/", include("support.urls")),
    path("policy/", include("policy.urls")),
    path("nayose/", include("nayose.urls")),
    path("grant/", include("grant.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__", include(
        debug_toolbar.urls))] + urlpatterns
