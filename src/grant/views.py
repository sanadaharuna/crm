from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, ListView

from .models import Project, Member


class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 10000
    template_name = "grant/project_list.html"

    def get_queryset(self):
        queryset = Member.objects.select_related().filter(role=1).order_by("project__nendo").reverse()
        return queryset


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["member_list"] = Member.objects.filter(
            project=pk).order_by("role", "shozoku", "shimei")
        context["member_count"] = Member.objects.filter(project=pk).count()
        return context
