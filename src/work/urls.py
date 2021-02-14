from django.urls import path

from . import views

app_name = "work"
urlpatterns = [
    path("", views.KeywordFrontView.as_view(), name="front"),
    path("list", views.KeywordListView.as_view(), name="list"),
    path("detail/<str:pk>/", views.KeywordDetailView.as_view(), name="detail"),
]
