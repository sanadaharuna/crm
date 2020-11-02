from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import DetailView, ListView

from .models import Attendee, Lecturer, Seminar


class SeminarListView(LoginRequiredMixin, ListView):
    paginate_by = 10000
    ordering = ["-kaisaibi", '-pk']

    def get_queryset(self):
        queryset = Seminar.objects.annotate(attendee_count=Count(
            "attendee")).order_by("kaisaibi").reverse()
        return queryset


class SeminarDetailView(LoginRequiredMixin, DetailView):
    model = Seminar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["attendee_list"] = Attendee.objects.filter(
            seminar=pk).order_by("shozoku", "shimei")
        context["lecturer_list"] = Lecturer.objects.filter(seminar=pk)
        context["attendee_count"] = Attendee.objects.filter(seminar=pk).count()
        return context
