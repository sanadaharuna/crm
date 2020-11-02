from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import DetailView, ListView

from .models import Policy, Participant


class PolicyListView(LoginRequiredMixin, ListView):
    paginate_by = 10000
    # ordering = ["-nendo", 'shisakumei']

    def get_queryset(self):
        queryset = Policy.objects.annotate(participant_count=Count(
            "participant")).order_by("id")
        return queryset


class PolicyDetailView(LoginRequiredMixin, DetailView):
    model = Policy
    ordering = ["-nendo", 'shozoku', "shimei"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["participant_list"] = Participant.objects.filter(
            policy=pk).order_by("-nendo", "shozoku", "shimei")
        context["participant_count"] = Participant.objects.filter(
            policy=pk).count()
        return context
