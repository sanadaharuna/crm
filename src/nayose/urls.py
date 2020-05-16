from django.urls import path
# from django_filters.views import FilterView

from nayose import views
# from nayose.models import Nayose

app_name = "nayose"
urlpatterns = [
    path("", views.NayoseFrontView.as_view(), name="front"),
    # path("list", views.NayoseListView.as_view(), name="list"),
    path("list", views.NayoseFilterView.as_view(), name="list"),
    path("create", views.NayoseCreateView.as_view(), name="create"),
    path("<int:pk>/detail", views.NayoseDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.NayoseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.NayoseDeleteView.as_view(), name="delete"),
]
