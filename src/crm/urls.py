from django.conf import settings
# from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path

# from django.conf.urls import url, static

urlpatterns = [
    path("", include("base.urls")),
    # path("researcher/", include("researcher.urls")),
    path("nayose/", include("nayose.urls")),
    # path("shokuinroku/", include("shokuinroku.urls")),
    path("accounts/", include("allauth.urls")),
    # path("application/", include("application.urls")),
    path("promotion/", include("promotion.urls")),
    path("seminar/", include("seminar.urls")),
    path("support/kaken/", include("kaken.urls")),
    path("support/consignment/", include("consignment.urls")),
    path("support/matching/", include("matching.urls")),
    path("reviewer/", include("reviewer.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__", include(
        debug_toolbar.urls))] + urlpatterns

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
