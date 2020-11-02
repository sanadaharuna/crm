from django.urls import path

from . import views

app_name = "policy"
urlpatterns = [
    path("", views.PolicyListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.PolicyDetailView.as_view(), name="detail"),
]
