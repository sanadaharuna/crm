from django.urls import path

from . import views

app_name = "matching"
urlpatterns = [
    path("", views.MatchingListView.as_view(), name="list"),
    path("create", views.MatchingCreateView.as_view(), name="create"),
    path("<int:pk>/", views.MatchingDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.MatchingUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.MatchingDeleteView.as_view(), name="delete"),
]

