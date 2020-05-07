from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Value, CharField
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import KakenForm, KakenSearchForm
from .models import Kaken


class KakenListView(LoginRequiredMixin, ListView):
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
        # 支援年度
        if self.request.GET.get("fiscalyear"):
            fiscalyear = self.request.GET.get("fiscalyear")
            queryset = queryset.filter(Q(fiscalyear=fiscalyear))
        # 担当者
        if self.request.GET.get("tantousha"):
            tantousha = self.request.GET.get("tantousha")
            queryset = queryset.filter(Q(tantousha__icontains=tantousha))
        return queryset


class KakenDetailView(LoginRequiredMixin, DetailView):
    model = Kaken


class KakenCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Kaken
    form_class = KakenForm
    success_message = "保存しました。"
    success_url = reverse_lazy("kaken:list")


class KakenUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Kaken
    form_class = KakenForm
    success_message = "保存しました。"
    success_url = reverse_lazy("kaken:list")


class KakenDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Kaken
    success_url = reverse_lazy("kaken:list")
    success_message = "削除しました。"
