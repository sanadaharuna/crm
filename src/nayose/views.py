from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Concat
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .forms import NayoseSearchForm
from .models import Nayose


class NayoseFrontView(LoginRequiredMixin, TemplateView):
    template_name = "nayose/nayose_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = NayoseSearchForm()
        return context


class NayoseListView(LoginRequiredMixin, ListView):
    paginate_by = 10000

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        if self.request.GET.get("q"):
            # 検索用に名寄せ氏名の姓と名をつなげる
            queryset = Nayose.objects.annotate(
                kanjishimei=Concat("kanjishimei_sei", "kanjishimei_mei"),
                kanashimei=Concat("kanashimei_sei", "kanashimei_mei"),
            )
            # 検索クエリの空白を削除する
            q = self.request.GET.get("q")
            q = q.strip()
            table = q.maketrans({"　": "", " ": ""})
            q = q.translate(table)
            # 検索する
            if q.isdecimal():
                queryset = queryset.filter(
                    Q(nayose_id=q)
                    | Q(erad_id=q)
                    | Q(shokuin_id=q)
                    | Q(hijoukin_id=q)
                )
            else:
                queryset = queryset.filter(
                    Q(kanjishimei__icontains=q)
                    | Q(kanashimei__icontains=q)
                )
            # カナ氏名でソートする
            queryset = queryset.order_by("kanashimei")
        else:
            queryset = Nayose.objects.none()
        return queryset
