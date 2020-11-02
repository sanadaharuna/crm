from django.urls import path

from nayose import views

app_name = "nayose"
urlpatterns = [
    path("", views.NayoseFrontView.as_view(), name="front"),
    path("list", views.NayoseListView.as_view(), name="list"),
]
