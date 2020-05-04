# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import NayoseForm, NayoseSearchForm
from .models import Nayose


class NayoseFrontView(TemplateView):
    template_name = "nayose/nayose_front.html"


class NayoseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = NayoseSearchForm(self.request.GET)
        else:
            context["search_form"] = NayoseSearchForm()
        return context

    def get_queryset(self):
        if self.request.GET:
            queryset = Nayose.objects.annotate(
                kanjishimei=Concat("kanjishimei_sei", "kanjishimei_mei"),
                kanashimei=Concat("kanashimei_sei", "kanashimei_mei"),
            )
            # 漢字氏名
            if self.request.GET.get("kanjishimei"):
                kanjishimei = self.request.GET.get("kanjishimei")
                queryset = queryset.filter(
                    Q(kanjishimei__icontains=kanjishimei))
            # カナ氏名
            if self.request.GET.get("kanashimei"):
                kanashimei = self.request.GET.get("kanashimei")
                queryset = queryset.filter(Q(kanashimei__icontains=kanashimei))
            queryset = queryset.order_by("kanashimei")
        else:
            queryset = Nayose.objects.none()
        return queryset


class NayoseDetailView(DetailView):
    model = Nayose


class NayoseCreateView(SuccessMessageMixin, CreateView):
    model = Nayose
    form_class = NayoseForm
    success_message = "保存しました。"
    success_url = reverse_lazy("nayose:list")


class NayoseUpdateView(SuccessMessageMixin, UpdateView):
    model = Nayose
    form_class = NayoseForm
    success_message = "保存しました。"
    success_url = reverse_lazy("nayose:list")


class NayoseDeleteView(SuccessMessageMixin, DeleteView):
    model = Nayose
    success_url = reverse_lazy("nayose:list")
    success_message = "削除しました。"
