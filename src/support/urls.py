from django.urls import path

from .views import KakenhiListView, CompetitiveFundListView, MatchingListView

app_name = "support"
urlpatterns = [
    path("kakenhi", KakenhiListView.as_view(), name="kakenhi"),
    path("competitivefund", CompetitiveFundListView.as_view(),
         name="competitivefund"),
    path("matching", MatchingListView.as_view(), name="matching"),
]
