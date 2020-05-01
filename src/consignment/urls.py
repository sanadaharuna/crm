from django.urls import path

from . import views

app_name = "consignment"
urlpatterns = [
    path("", views.ConsignmentListView.as_view(), name="list"),
    path("create", views.ConsignmentCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ConsignmentDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.ConsignmentUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.ConsignmentDeleteView.as_view(), name="delete"),
]
