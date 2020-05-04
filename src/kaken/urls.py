from django.urls import path

from . import views

app_name = "kaken"
urlpatterns = [
    path("", views.KakenListView.as_view(), name="list"),
    path("create", views.KakenCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.KakenUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.KakenDeleteView.as_view(), name="delete"),
]
