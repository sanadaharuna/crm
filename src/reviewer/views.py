# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ReviewerSearchForm, ReviewerForm
from .models import Reviewer


class ReviewerListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = ReviewerSearchForm(self.request.GET)
        else:
            context["search_form"] = ReviewerSearchForm()
        return context

    def get_queryset(self):
        queryset = Reviewer.objects.all()
        # 年度
        if self.request.GET.get("fiscalyear"):
            fiscalyear = self.request.GET.get("fiscalyear")
            queryset = queryset.filter(Q(fiscalyear=fiscalyear))
        # 氏名
        if self.request.GET.get("name"):
            name = self.request.GET.get("name")
            queryset = queryset.filter(Q(name_icontains=name))
        # 委員会
        if self.request.GET.get("committee"):
            committee = self.request.GET.get("committee")
            queryset = queryset.filter(Q(committee__icontains=committee))
        # 表彰
        if self.request.GET.get("is_awarded"):
            is_awarded = bool(self.request.GET.get("is_awarded"))
            queryset = queryset.filter(Q(is_awarded=is_awarded))
        return queryset


class ReviewerCreateView(SuccessMessageMixin, CreateView):
    model = Reviewer
    form_class = ReviewerForm
    success_message = "保存しました。"
    success_url = reverse_lazy("reviewer:list")


class ReviewerUpdateView(SuccessMessageMixin, UpdateView):
    model = Reviewer
    form_class = ReviewerForm
    success_message = "保存しました。"
    success_url = reverse_lazy("reviewer:list")


class ReviewerDeleteView(SuccessMessageMixin, DeleteView):
    model = Reviewer
    success_url = reverse_lazy("reviewer:list")
    success_message = "削除しました。"
