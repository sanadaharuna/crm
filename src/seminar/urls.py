from django.urls import path

from . import views

app_name = "seminar"
urlpatterns = [
    # SeminarモデルのCRUD
    path("", views.SeminarListView.as_view(), name="list"),
    path("<int:pk>/", views.SeminarDetailView.as_view(), name="detail"),
    path("create", views.SeminarCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.SeminarUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.SeminarDeleteView.as_view(), name="delete"),
    # AttendeeモデルのCRUD
    path("attendee/create", views.AttendeeCreateView.as_view(), name="attendee_create"),
    path(
        "attendee/<int:pk>/update",
        views.AttendeeUpdateView.as_view(),
        name="attendee_update",
    ),
    path(
        "attendee/<int:pk>/delete",
        views.AttendeeDeleteView.as_view(),
        name="attendee_delete",
    ),
    # LecturerモデルのCRUD
    path("lecturer/create", views.LecturerCreateView.as_view(), name="lecturer_create"),
    path(
        "lecturer/<int:pk>/update",
        views.LecturerUpdateView.as_view(),
        name="lecturer_update",
    ),
    path(
        "lecturer/<int:pk>/delete",
        views.LecturerDeleteView.as_view(),
        name="lecturer_delete",
    ),
]
