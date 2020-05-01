
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import AttendeeForm, LecturerForm, SeminarForm, SeminarSearchForm
from .models import Seminar, Attendee, Lecturer

#
# SeminarモデルのCRUD
#


class SeminarListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["search_form"] = SeminarSearchForm(self.request.GET)
        else:
            context["search_form"] = SeminarSearchForm()
        return context

    def get_queryset(self):
        queryset = Seminar.objects.annotate(
            count=Count("attendee")).order_by("-date")
        # 支援年度
        if self.request.GET.get("fiscalyear"):
            fiscalyear = self.request.GET.get("fiscalyear")
            queryset = queryset.filter(Q(fiscalyear=fiscalyear))
        # 催事名
        if self.request.GET.get("title"):
            title = self.request.GET.get("title")
            queryset = queryset.filter(Q(title__icontains=title))
        # 会場
        if self.request.GET.get("venue"):
            venue = self.request.GET.get("venue")
            queryset = queryset.filter(Q(venue__icontains=venue))
        return queryset


class SeminarDetailView(DetailView):
    model = Seminar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["attendee_list"] = Attendee.objects.filter(
            seminar=self.kwargs.get("pk")
        )
        context["lecturer_list"] = Lecturer.objects.filter(
            seminar=self.kwargs.get("pk")
        )
        return context


class SeminarCreateView(SuccessMessageMixin, CreateView):
    model = Seminar
    form_class = SeminarForm
    success_message = "登録しました。"
    success_url = reverse_lazy("seminar:list")


class SeminarUpdateView(SuccessMessageMixin, UpdateView):
    model = Seminar
    form_class = SeminarForm
    success_message = "変更しました。"
    success_url = reverse_lazy("seminar:list")


class SeminarDeleteView(SuccessMessageMixin, DeleteView):
    model = Seminar
    success_message = "削除しました。"
    success_url = reverse_lazy("seminar:list")


#
# AttendeeモデルのCRUD
#


class AttendeeCreateView(SuccessMessageMixin, CreateView):
    model = Attendee
    form_class = AttendeeForm
    success_message = "登録しました。"
    template_name = "seminar/attendance_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seminar"] = Seminar.objects.get(
            pk=self.request.GET.get("seminar_id"))
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial["seminar"] = self.request.GET.get("seminar_id")
        return initial

    def get_success_url(self):
        return reverse("seminar:detail", kwargs={"pk": self.object.seminar_id})


class AttendeeUpdateView(SuccessMessageMixin, UpdateView):
    model = Attendee
    form_class = AttendeeForm
    success_message = "変更しました。"
    template_name = "seminar/attendance_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seminar"] = Seminar.objects.get(pk=self.object.seminar_id)
        return context

    def get_success_url(self):
        return reverse("seminar:detail", kwargs={"pk": self.object.seminar_id})


class AttendeeDeleteView(SuccessMessageMixin, DeleteView):
    model = Attendee
    success_message = "削除しました。"

    def get_success_url(self):
        return reverse("seminar:detail", kwargs={"pk": self.object.seminar_id})


#
# LecturerモデルのCRUD
#


class LecturerCreateView(AttendeeCreateView):
    model = Lecturer
    form_class = LecturerForm


class LecturerUpdateView(AttendeeUpdateView):
    model = Lecturer
    form_class = LecturerForm


class LecturerDeleteView(AttendeeDeleteView):
    model = Lecturer
