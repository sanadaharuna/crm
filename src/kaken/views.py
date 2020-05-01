# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Value, CharField
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import KakenForm, KakenSearchForm
from .models import Kaken


class KakenListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = KakenSearchForm(self.request.GET)
        else:
            context["search_form"] = KakenSearchForm()
        return context

    def get_queryset(self):
        queryset = Kaken.objects.annotate(
            tantousha=Concat(
                "shutantou", Value(" / "), "fukutantou", output_field=CharField()
            )
        )
        # 支援種別
        if self.request.GET.get("support_type"):
            support_type = self.request.GET.get("support_type")
            queryset = queryset.filter(Q(support_type=support_type))
        # 支援年度
        if self.request.GET.get("fiscalyear"):
            fiscalyear = self.request.GET.get("fiscalyear")
            queryset = queryset.filter(Q(fiscalyear=fiscalyear))
        # 担当者
        if self.request.GET.get("tantousha"):
            tantousha = self.request.GET.get("tantousha")
            queryset = queryset.filter(Q(tantousha__icontains=tantousha))
        # 完了日が空欄
        if self.request.GET.get("in_progress"):
            in_progress = bool(self.request.GET.get("in_progress"))
            queryset = queryset.filter(Q(date_completed__isnull=in_progress))
        return queryset


class KakenDetailView(DetailView):
    model = Kaken


class KakenCreateView(SuccessMessageMixin, CreateView):
    model = Kaken
    form_class = KakenForm
    success_message = "保存しました。"
    success_url = reverse_lazy("kaken:list")


class KakenUpdateView(SuccessMessageMixin, UpdateView):
    model = Kaken
    form_class = KakenForm
    success_message = "保存しました。"
    success_url = reverse_lazy("kaken:list")


class KakenDeleteView(SuccessMessageMixin, DeleteView):
    model = Kaken
    success_url = reverse_lazy("kaken:list")
    success_message = "削除しました。"
