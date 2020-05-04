import factory
import factory.fuzzy
import factory.django
from nayose.models import Nayose


class NayoseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Nayose

    nayose_id = factory.Sequence(lambda n: "%09d" % n)
    erad_id = factory.Sequence(lambda n: "%08d" % n)
    shokuin_id = factory.Sequence(lambda n: "%08d" % n)
    hijoukin_id = factory.Sequence(lambda n: "%08d" % n)
    kanjishimei_sei = factory.Faker("last_name", locale="ja_jp")
    kanjishimei_mei = factory.Faker("first_name", locale="ja_jp")
    kanashimei_sei = factory.Faker("last_kana_name", locale="ja_jp")
    kanashimei_mei = factory.Faker("first_kana_name", locale="ja_jp")
    date_of_birth = factory.Faker("date")
    sex = factory.fuzzy.FuzzyChoice(Nayose.SEX_CHOICES, getter=lambda c: c[0])
