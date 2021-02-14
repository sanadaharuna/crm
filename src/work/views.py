from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import DetailView, ListView

from .forms import KeywordSearchForm
from .models import Keyword


class KeywordFrontView(LoginRequiredMixin, ListView):
    template_name = "work/keyword_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = KeywordSearchForm()
        return context

    def get_queryset(self):
        queryset = Keyword.objects.values("bukyokumei").annotate(cnt=Count(
            "bukyokumei")).order_by("-cnt")
        return queryset


class KeywordListView(LoginRequiredMixin, ListView):
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        queryset = Keyword.objects.all()
        if self.request.GET.get("q"):
            # 検索クエリ内の空白文字を削除する
            q = self.request.GET.get("q").strip()
            table = str.maketrans({"　": "", " ": ""})
            q = q.translate(table)
            # 検索する
            queryset = queryset.filter(keyword__icontains=q)
        queryset = queryset.order_by("kanashimei")
        return queryset


class KeywordDetailView(LoginRequiredMixin, DetailView):
    model = Keyword

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nayose"] = Keyword.objects.values("bukyokumei").annotate(cnt=Count(
            "bukyokumei")).order_by("-cnt")
        return context
