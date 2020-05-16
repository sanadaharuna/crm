import django_filters
from nayose.models import Nayose


class NayoseFilter(django_filters.FilterSet):
    class Meta:
        model = Nayose
