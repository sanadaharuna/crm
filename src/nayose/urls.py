from django.urls import path

from . import views

app_name = "nayose"
urlpatterns = [
    path("", views.NayoseListView.as_view(), name="list"),
    path("create", views.NayoseCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.NayoseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.NayoseDeleteView.as_view(), name="delete"),
]
