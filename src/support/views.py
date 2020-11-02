from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import CompetitiveFund, Kakenhi, Matching


class KakenhiListView(LoginRequiredMixin, ListView):
    model = Kakenhi
    paginate_by = 10000
    ordering = ["-uketsukebi", '-pk']


class CompetitiveFundListView(LoginRequiredMixin, ListView):
    model = CompetitiveFund
    paginate_by = 10000
    ordering = ["-uketsukebi", '-pk']


class MatchingListView(LoginRequiredMixin, ListView):
    model = Matching
    paginate_by = 10000
    ordering = ["-uketsukebi", '-pk']
