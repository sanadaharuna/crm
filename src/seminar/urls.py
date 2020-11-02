from django.urls import path

from . import views

app_name = "seminar"
urlpatterns = [
    path("", views.SeminarListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.SeminarDetailView.as_view(), name="detail"),
]
