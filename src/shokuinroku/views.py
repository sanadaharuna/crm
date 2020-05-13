from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from .forms import ShokuinSearchForm
from .models import Shokuin


class ShokuinFrontView(LoginRequiredMixin, TemplateView):
    template_name = "shokuinroku/shokuinroku_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ShokuinSearchForm()
        context["q"] = self.request.GET.get("q")
        return context


class ShokuinListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        if self.request.GET.get("q"):
            q = self.request.GET.get("q")
            # 基準日で検索する
            queryset = Shokuin.objects.filter(kijunbi=q)
            # カナ氏名でソートする
            queryset = queryset.order_by("furigana")
        else:
            queryset = Shokuin.objects.none()
        return queryset
