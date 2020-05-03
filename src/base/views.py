from django.views.generic import RedirectView
from django.urls import reverse_lazy


class FrontPageView(RedirectView):
    url = reverse_lazy("nayose:list")
