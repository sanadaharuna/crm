from django.urls import path

from .views import FrontPageView


app_name = "base"
urlpatterns = [path("", FrontPageView.as_view(), name="front")]
