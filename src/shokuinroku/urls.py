from django.urls import path

from . import views

app_name = "shokuinroku"
urlpatterns = [
    path("", views.ShokuinListView.as_view(), name="list"),
    # path("import", views.ShokuinImportView.as_view(), name="import"),
]
