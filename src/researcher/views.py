# import csv
# import io

# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Q
# from django.db.models.functions import Concat
# from django.urls import reverse_lazy
# from django.views.generic import DetailView, FormView, ListView
# from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

# from consignment.models import Consignment
# from kaken.models import Kaken
# from matching.models import Matching
# from promotion.models import Candidate
# from reviewer.models import Reviewer
# from seminar.models import Attendee, Lecturer

# from .forms import ResearcherSearchForm, ResearcherUploadForm
from .forms import ResearcherSearchForm
from .models import Researcher


class ResearcherFrontView(LoginRequiredMixin, TemplateView):
    template_name = "researcher/researcher_front.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ResearcherSearchForm()
        context["q"] = self.request.GET.get("q")
        return context


class ResearcherListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        if self.request.GET.get("q"):
            q = self.request.GET.get("q")
            # 基準日で検索する
            queryset = Researcher.objects.filter(as_of=q)
            # カナ氏名でソートする
            queryset = queryset.order_by("furigana")
        else:
            queryset = Researcher.objects.none()
        return queryset


# class ResearcherListView(ListView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.GET:
#             context["search_form"] = ResearcherSearchForm(self.request.GET)
#         else:
#             context["search_form"] = ResearcherSearchForm()
#         return context

#     def get_queryset(self):
#         if self.request.GET:
#             queryset = Researcher.objects.annotate(
#                 kanjishimei=Concat("kanjishimei_sei", "kanjishimei_mei"),
#                 kanashimei=Concat("kanashimei_sei", "kanashimei_mei"),
#             )
#         else:
#             queryset = Researcher.objects.none()
#         # 漢字氏名
#         if self.request.GET.get("kanjishimei"):
#             kanjishimei = self.request.GET.get("kanjishimei")
#             queryset = queryset.filter(Q(kanjishimei__icontains=kanjishimei))
#         # カナ氏名
#         if self.request.GET.get("kanashimei"):
#             kanashimei = self.request.GET.get("kanashimei")
#             queryset = queryset.filter(Q(kanashimei__icontains=kanashimei))
#         return queryset

# class ResearcherDetailView(DetailView):
#     model = Researcher

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         researcher_id = self.kwargs.get("pk")
#         context["kaken_list"] = Kaken.objects.filter(researcher=researcher_id)
#         context["consignment_list"] = Consignment.objects.filter(
#             researcher=researcher_id
#         )
#         context["matching_list"] = Matching.objects.filter(
#             researcher=researcher_id)

#         context["attendee_list"] = Attendee.objects.select_related("seminar").filter(
#             researcher=researcher_id
#         )
#         context["lecturer_list"] = Lecturer.objects.select_related("seminar").filter(
#             researcher=researcher_id
#         )
#         context["candidate_list"] = Candidate.objects.select_related(
#             "promotion"
#         ).filter(researcher=researcher_id)
#         context["reviewer_list"] = Reviewer.objects.filter(
#             nayose_id=researcher_id)
#         return context


# class ResearcherImportView(SuccessMessageMixin, FormView):
#     template_name = "researcher/import.html"
#     success_url = reverse_lazy("researcher:list")
#     form_class = ResearcherUploadForm
#     success_message = "登録しました。"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form_name"] = "researcher"
#         return context

#     def form_valid(self, form):
#         # CSVファイルを取り込む
#         csvfile = io.TextIOWrapper(form.cleaned_data["file"])
#         reader = csv.reader(csvfile)
#         # 冒頭2行をスキップする
#         header = next(reader)
#         header = next(reader)
#         # 既存のデータを削除する
#         Researcher.objects.all().delete()
#         # 新規データを登録する
#         objs = [
#             Researcher(
#                 researcher_id=row[0],
#                 kanjishimei_sei=row[3],
#                 kanjishimei_mei=row[4],
#                 kanashimei_sei=row[5],
#                 kanashimei_mei=row[6],
#                 date_of_birth=(row[11][:4] + "-" +
#                                row[11][4:6] + "-" + row[11][6:]),
#                 sex=row[12],
#                 department=row[42],
#                 title=row[44],
#             )
#             for row in reader
#         ]
#         Researcher.objects.bulk_create(objs)
#         return super().form_valid(form)
