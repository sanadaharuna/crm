from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


admin.site.site_title = "Galette CRM"
admin.site.site_header = "Galette CRM"

urlpatterns = [
    path("", RedirectView.as_view(permanent=False, url="erad/")),
    path("erad/", include("erad.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("data_management/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__", include(
        debug_toolbar.urls))] + urlpatterns
