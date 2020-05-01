import csv
import io
from datetime import date

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .forms import ApplicationUploadForm
from .models import Application


class ApplicationListView(ListView):
    model = Application


class ApplicationImportView(SuccessMessageMixin, FormView):
    template_name = "application/import.html"
    success_url = reverse_lazy("application:list")
    form_class = ApplicationUploadForm
    success_message = "登録しました。"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "application"
        return context

    def form_valid(self, form):
        # CSVファイルを取り込む
        csvfile = io.TextIOWrapper(form.cleaned_data["file"])
        reader = csv.reader(csvfile)
        # 冒頭2行をスキップする
        header = next(reader)
        header = next(reader)
        # 既存のデータを削除する
        Application.objects.all().delete()
        # 新規データを登録する
        objs = [
            Application(
                nendo=row[5],
                seido_code=row[6],
                seidomei=row[7],
                jigyou_code=row[8],
                jigyoumei=row[9],
                koubogroup_code=row[10],
                koubogroupmei=row[11],
                koubo_code=row[12],
                koubomei=row[13],
                kenkyuukaihatsukadaimei=row[18],
                gyoumu_main_status=row[22],
                researcher_id=row[45],
                shimeikanji_sei=row[46],
                shimeikanji_mei=row[47],
                kenkyuukikan_code=row[50],
                kenkyuukikanmei=row[51],
                bukyoku_code=row[52],
                bukyokumei=row[53],
                shokukai_code=row[54],
                yakushoku=row[55],
            )
            for row in reader
        ]
        Application.objects.bulk_create(objs)
        return super().form_valid(form)
