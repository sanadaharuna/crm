import factory
from datetime import date
from nayose.models import Nayose


class NayoseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Nayose

    erad_id = factory.Sequence(lambda n: "%09d" % n)
    shokuin_id = factory.Sequence(lambda n: "%08d" % n)
    hijoukin_id = factory.Sequence(lambda n: "%08d" % n)
    kanjishimei_sei = factory.Sequence(lambda n: "漢字姓%s" % n)
    kanjishimei_mei = factory.Sequence(lambda n: "漢字名%s" % n)
    kanashimei_sei = factory.Sequence(lambda n: "カナ姓%s" % n)
    kanashimei_mei = factory.Sequence(lambda n: "カナ名%s" % n)
    date_of_birth = date(1978, 2, 18)
    # sex = factory.fuzzy.FuzzyChoice(Nayose.SEX_CHOICES, getter=lambda c: c[0])
    sex = factory.FuzzyChoice(Nayose.SEX_CHOICES, getter=lambda c: c[0])
