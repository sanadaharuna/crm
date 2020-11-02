from django.urls import path

from erad import views

app_name = "erad"
urlpatterns = [
    path("", views.ResearcherFrontView.as_view(), name="front"),
    path("list", views.ResearcherListView.as_view(), name="list"),
    path("detail/<str:pk>/", views.ResearcherDetailView.as_view(), name="detail"),
]
