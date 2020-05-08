# import csv
# import io
# import unicodedata
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.urls import reverse_lazy
# from django.views.generic import FormView, ListView
from django.views.generic import ListView


# from .forms import ShokuinUploadForm
from .models import Shokuin


class ShokuinListView(LoginRequiredMixin, ListView):
    model = Shokuin


# class ShokuinImportView(FormView):
#     template_name = "shokuinroku/import.html"
#     success_url = reverse_lazy("shokuinroku:list")
#     form_class = ShokuinUploadForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form_name"] = "shokuin"
#         return context

#     def form_valid(self, form):
#         csvfile = io.TextIOWrapper(form.cleaned_data["file"])
#         reader = csv.reader(csvfile)
#         header = next(reader)
#         for row in reader:
#             data = {
#                 "shokuin_id": row[0],
#                 "shozokumei": row[1],
#                 "kakarikouzamei": row[2],
#                 "shokumei": row[3],
#                 "kanjishimei": row[4],
#                 "furigana": unicodedata.normalize("NFKC", row[5]),
#                 "naisenbangou": row[6],
#                 "mail_address": row[7],
#             }
#             Shokuin.objects.update_or_create(shokuin_id=row[0], defaults=data)
#         return super().form_valid(form)
