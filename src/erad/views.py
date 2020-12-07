from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views.generic import DetailView, ListView
from grant.models import Member
from nayose.models import Nayose
from attribute.models import Eligible
from event.models import Attendee
from support.models import CompetitiveFund, Kakenhi, Matching

from .forms import ResearcherSearchForm
from .models import Application, Researcher


class ResearcherFrontView(LoginRequiredMixin, ListView):
    template_name = "erad/researcher_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ResearcherSearchForm()
        return context

    def get_queryset(self):
        queryset = Researcher.objects.values("bukyokumei").annotate(cnt=Count(
            "bukyokumei")).order_by("-cnt")
        return queryset


class ResearcherListView(LoginRequiredMixin, ListView):
    paginate_by = 10000

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shimei"] = self.request.GET.get("shimei")
        context["shozoku"] = self.request.GET.get("shozoku")
        return context

    def get_queryset(self):
        queryset = Researcher.objects.all()
        if self.request.GET.get("shimei"):
            # 検索クエリ内の空白文字を削除する
            shimei = self.request.GET.get("shimei").strip()
            table = str.maketrans({"　": "", " ": ""})
            shimei = shimei.translate(table)
            # 検索する
            queryset = queryset.filter(
                Q(kanjishimei__icontains=shimei)
                | Q(kanashimei__icontains=shimei)
                | Q(tsuushoumei__icontains=shimei)
                | Q(eijishimei__icontains=shimei)
            )
        if self.request.GET.get("shozoku"):
            shozoku = self.request.GET.get("shozoku")
            queryset = queryset.filter(bukyokumei__icontains=shozoku)
        queryset = queryset.order_by("kanashimei")
        return queryset


class ResearcherDetailView(LoginRequiredMixin, DetailView):
    model = Researcher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["nayose"] = Nayose.objects.get(eradcode=pk)
        context["attendee_list"] = Attendee.objects.select_related().filter(
            eradcode=pk)
        context["support_kakenhi_list"] = Kakenhi.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["support_competitivefund_list"] = CompetitiveFund.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["support_matching_list"] = Matching.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["attribute_list"] = Eligible.objects.select_related().filter(
            eradcode=pk).order_by("nendo").reverse()
        context["grant_member_list"] = Member.objects.select_related().filter(
            eradcode=pk).order_by("project__nendo").reverse()
        context["kakenhi_list"] = Application.objects.filter(
            eradcode=pk).filter(seido_code="S000003").order_by("nendo").reverse()
        context["erad_list"] = Application.objects.filter(
            eradcode=pk).exclude(seido_code="S000003").order_by("nendo").reverse()
        return context
