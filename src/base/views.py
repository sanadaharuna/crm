from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# class FrontView(LoginRequiredMixin, TemplateView):
#     template_name = "base/front.html"


class FrontView(TemplateView):
    template_name = "base/front.html"
