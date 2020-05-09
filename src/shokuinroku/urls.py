from django.urls import path

from . import views

app_name = "shokuinroku"
urlpatterns = [
    path("", views.ShokuinFrontView.as_view(), name="front"),
    path("list", views.ShokuinListView.as_view(), name="list"),
]
