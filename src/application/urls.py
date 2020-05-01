from django.urls import path

from . import views

app_name = "application"
urlpatterns = [
    path("list", views.ApplicationListView.as_view(), name="list"),
    path("import", views.ApplicationImportView.as_view(), name="import"),
]
