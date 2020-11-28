from django.urls import path

from . import views

app_name = "grant"
urlpatterns = [
    path("", views.ProjectListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
]
