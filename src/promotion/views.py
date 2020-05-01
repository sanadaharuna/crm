
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CandidateForm, PromotionForm, PromotionSearchForm
from .models import Candidate, Promotion


class PromotionListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = PromotionSearchForm(self.request.GET)
        else:
            context["search_form"] = PromotionSearchForm()
        return context

    def get_queryset(self):
        queryset = Promotion.objects.all()
        # 支援年度
        if self.request.GET.get("fiscalyear"):
            fiscalyear = self.request.GET.get("fiscalyear")
            queryset = queryset.filter(Q(fiscalyear=fiscalyear))
        # 催事名
        if self.request.GET.get("title"):
            title = self.request.GET.get("title")
            queryset = queryset.filter(Q(title__icontains=title))
        return queryset


class PromotionDetailView(DetailView):
    model = Promotion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidate_list"] = Candidate.objects.filter(
            promotion=self.kwargs.get("pk")
        )
        context["count"] = Candidate.objects.filter(
            promotion=self.kwargs.get("pk")
        ).count()
        return context


class PromotionCreateView(SuccessMessageMixin, CreateView):
    model = Promotion
    form_class = PromotionForm
    success_message = "登録しました。"
    success_url = reverse_lazy("promotion:list")


class PromotionUpdateView(SuccessMessageMixin, UpdateView):
    model = Promotion
    form_class = PromotionForm
    success_message = "変更しました。"
    success_url = reverse_lazy("promotion:list")


class PromotionDeleteView(SuccessMessageMixin, DeleteView):
    model = Promotion
    success_message = "削除しました。"
    success_url = reverse_lazy("promotion:list")


#
# CandidateモデルのCRUD
#


class CandidateCreateView(SuccessMessageMixin, CreateView):
    model = Candidate
    form_class = CandidateForm
    success_message = "登録しました。"
    template_name = "promotion/candidate_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["promotion"] = Promotion.objects.get(
            pk=self.request.GET.get("promotion_id")
        )
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial["promotion"] = self.request.GET.get("promotion_id")
        return initial

    def get_success_url(self):
        return reverse("promotion:detail", kwargs={"pk": self.object.promotion_id})


class CandidateUpdateView(SuccessMessageMixin, UpdateView):
    model = Candidate
    form_class = CandidateForm
    success_message = "変更しました。"
    template_name = "promotion/candidate_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["promotion"] = Promotion.objects.get(
            pk=self.object.promotion_id)
        return context

    def get_success_url(self):
        return reverse("promotion:detail", kwargs={"pk": self.object.promotion_id})


class CandidateDeleteView(SuccessMessageMixin, DeleteView):
    model = Candidate
    success_message = "削除しました。"

    def get_success_url(self):
        return reverse("promotion:detail", kwargs={"pk": self.object.promotion_id})
