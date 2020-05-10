from django.urls import path

from . import views

app_name = "researcher"
urlpatterns = [
    path("", views.ResearcherFrontView.as_view(), name="front"),
    path("list", views.ResearcherListView.as_view(), name="list"),
    # path("<int:pk>/", views.ResearcherDetailView.as_view(), name="detail"),
    # path("import", views.ResearcherImportView.as_view(), name="import"),
]
