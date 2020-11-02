from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Concat
from django.views.generic import DetailView, ListView, TemplateView
from nayose.models import Nayose
from policy.models import Participant
from seminar.models import Attendee, Lecturer
from support.models import CompetitiveFund, Kakenhi, Matching
from grant.models import Member

from .forms import ResearcherSearchForm
from .models import Application, Researcher


class ResearcherFrontView(LoginRequiredMixin, TemplateView):
    template_name = "erad/researcher_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ResearcherSearchForm()
        return context


class ResearcherListView(LoginRequiredMixin, ListView):
    paginate_by = 10000

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        if self.request.GET.get("q"):
            # 検索用に名寄せ氏名の姓と名をつなげる
            queryset = Researcher.objects.annotate(
                kanjishimei=Concat("kenkyuushashimei_sei",
                                   "kenkyuushashimei_mei"),
                kanashimei=Concat("furigana_sei", "furigana_mei"),
                tsuushoumei=Concat("tsuushoumei_sei", "tsuushoumei_mei"),
                tsuushoumei_kana=Concat(
                    "tsuushoumeifurigana_sei", "tsuushoumeifurigana_mei"),
                eijishimei=Concat("eiji_sei", "eiji_mei")
            )
            # 検索クエリ内の空白文字を削除する
            q = self.request.GET.get("q")
            q = q.strip()
            table = q.maketrans({"　": "", " ": ""})
            q = q.translate(table)
            # 検索する
            if q.isdecimal():
                queryset = queryset.filter(eradcode=q)
            else:
                queryset = queryset.filter(
                    Q(kanjishimei__icontains=q)
                    | Q(kanashimei__icontains=q)
                    | Q(tsuushoumei__icontains=q)
                    | Q(eijishimei__icontains=q)
                )
            # カナ氏名でソートする
            queryset = queryset.order_by("kanashimei")
        else:
            queryset = Researcher.objects.none()
        return queryset


class ResearcherDetailView(LoginRequiredMixin, DetailView):
    model = Researcher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["nayose"] = Nayose.objects.get(eradcode=pk)
        context["lecturer_list"] = Lecturer.objects.select_related().filter(
            eradcode=pk)
        context["attendee_list"] = Attendee.objects.select_related().filter(
            eradcode=pk)
        context["support_kakenhi_list"] = Kakenhi.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["support_competitivefund_list"] = CompetitiveFund.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["support_matching_list"] = Matching.objects.filter(
            eradcode=pk).order_by("uketsukebi").reverse()
        context["participant_list"] = Participant.objects.select_related().filter(
            eradcode=pk).order_by("nendo").reverse()
        context["grant_member_list"] = Member.objects.select_related().filter(
            eradcode=pk).order_by("project__nendo").reverse()
        context["kakenhi_list"] = Application.objects.filter(
            eradcode=pk).filter(seido_code="S000003").order_by("nendo").reverse()
        context["erad_list"] = Application.objects.filter(
            eradcode=pk).exclude(seido_code="S000003").order_by("nendo").reverse()
        return context
