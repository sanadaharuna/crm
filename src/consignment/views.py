# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import CharField, Q, Value
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ConsignmentForm, ConsignmentSearchForm
from .models import Consignment


class ConsignmentListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = ConsignmentSearchForm(self.request.GET)
        else:
            context["search_form"] = ConsignmentSearchForm()
        return context

    def get_queryset(self):
        queryset = Consignment.objects.annotate(
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
        # 完了日が空欄
        if self.request.GET.get("in_progress"):
            in_progress = bool(self.request.GET.get("in_progress"))
            queryset = queryset.filter(Q(date_completed__isnull=in_progress))
        return queryset


class ConsignmentDetailView(DetailView):
    model = Consignment


class ConsignmentCreateView(SuccessMessageMixin, CreateView):
    model = Consignment
    form_class = ConsignmentForm
    success_message = "保存しました。"
    success_url = reverse_lazy("consignment:list")


class ConsignmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Consignment
    form_class = ConsignmentForm
    success_message = "保存しました。"
    success_url = reverse_lazy("consignment:list")


class ConsignmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Consignment
    success_url = reverse_lazy("consignment:list")
    success_message = "削除しました。"
