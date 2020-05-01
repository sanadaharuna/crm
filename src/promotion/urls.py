from django.urls import path

from . import views

app_name = "promotion"
urlpatterns = [
    # PromotionモデルのCRUD
    path("", views.PromotionListView.as_view(), name="list"),
    path("<int:pk>/", views.PromotionDetailView.as_view(), name="detail"),
    path("create", views.PromotionCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.PromotionUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.PromotionDeleteView.as_view(), name="delete"),
    # CandidateモデルのCRUD
    path(
        "candidate/create", views.CandidateCreateView.as_view(), name="candidate_create"
    ),
    path(
        "candidate/<int:pk>/update",
        views.CandidateUpdateView.as_view(),
        name="candidate_update",
    ),
    path(
        "candidate/<int:pk>/delete",
        views.CandidateDeleteView.as_view(),
        name="candidate_delete",
    ),
]
