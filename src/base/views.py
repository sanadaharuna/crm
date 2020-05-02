# from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin


# class FrontPageView(TemplateView):
#     template_name = "base/front.html"


class FrontPageView(RedirectView):
    url = reverse_lazy("nayose:list")
