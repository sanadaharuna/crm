from django.urls import path
from django.views.generic import TemplateView

from .views import FrontView

# from . import views

app_name = "base"
urlpatterns = [path("", FrontView.as_view(), name="front")]
