import django_filters
from nayose.models import Nayose


class NayoseFilter(django_filters.FilterSet):
    # nayose_id = django_filters.NumberFilter()

    class Meta:
        model = Nayose
        fields = ["nayose_id", "shokuin_id"]
