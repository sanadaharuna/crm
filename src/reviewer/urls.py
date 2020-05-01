from django.urls import path

from . import views

app_name = "reviewer"
urlpatterns = [
    path("", views.ReviewerListView.as_view(), name="list"),
    path("create", views.ReviewerCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.ReviewerUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.ReviewerDeleteView.as_view(), name="delete"),
]
