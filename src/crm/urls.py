from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("base.urls")),
    path("nayose/", include("nayose.urls")),
    path("accounts/", include("allauth.urls")),
    # path("promotion/", include("promotion.urls")),
    # path("seminar/", include("seminar.urls")),
    path("kaken/", include("kaken.urls")),
    # path("consignment/", include("consignment.urls")),
    # path("matching/", include("matching.urls")),
    # path("reviewer/", include("reviewer.urls")),
    path("admin/", admin.site.urls),
    path("shokuinroku/", include("shokuinroku.urls")),
    # path("researcher/", include("researcher.urls")),
    # path("application/", include("application.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__", include(
        debug_toolbar.urls))] + urlpatterns
