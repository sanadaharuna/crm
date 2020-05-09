from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Concat
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import NayoseForm, NayoseSearchForm
from .models import Nayose
from shokuinroku.models import Shokuin


class NayoseFrontView(LoginRequiredMixin, TemplateView):
    template_name = "nayose/nayose_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = NayoseSearchForm()
        context["q"] = self.request.GET.get("foundation")
        return context


class NayoseListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        if self.request.GET.get("q"):
            # 研究者検索画面用
            # 姓と名をつなげる
            queryset = Nayose.objects.annotate(
                kanjishimei=Concat("kanjishimei_sei", "kanjishimei_mei"),
                kanashimei=Concat("kanashimei_sei", "kanashimei_mei"),
            )
            # 検索語の空白を削除する
            q = self.request.GET.get("q")
            q = q.strip()
            table = q.maketrans({"　": "", " ": ""})
            q = q.translate(table)
            # 各種番号を検索する
            if q.isdecimal():
                queryset = queryset.filter(Q(nayose_id=q) | Q(
                    erad_id=q) | Q(shokuin_id=q) | Q(hijoukin_id=q))
            # 氏名を検索する
            else:
                queryset = queryset.filter(
                    Q(kanjishimei__icontains=q) | Q(kanashimei__icontains=q))
            # カナ氏名でソートする
            queryset = queryset.order_by("kanashimei")
        elif self.request.GET.get("shokuin_id"):
            shokuin_id = self.request.GET.get("shokuin_id")
            queryset = Nayose.objects.filter(shokuin_id=shokuin_id)
        else:
            queryset = Nayose.objects.none()
        return queryset


class NayoseDetailView(LoginRequiredMixin, DetailView):
    model = Nayose

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # shokuin_id = self.kwargs.get("shokuin_id")
        context["shokuinroku"] = Shokuin.objects.filter(
            shokuin_id="00000001").order_by("as_of").reverse().first()
        return context


class NayoseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Nayose
    form_class = NayoseForm
    success_message = "保存しました。"
    success_url = reverse_lazy("nayose:list")


class NayoseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Nayose
    form_class = NayoseForm
    success_message = "保存しました。"
    success_url = reverse_lazy("nayose:list")


class NayoseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Nayose
    success_url = reverse_lazy("nayose:list")
    success_message = "削除しました。"
