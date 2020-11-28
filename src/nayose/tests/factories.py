import factory
import factory.django
import factory.fuzzy

from nayose.models import Nayose, Shokuin


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


class ShokuinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shokuin

    kijunbi = factory.Faker("date")
    shokuin_id = factory.Sequence(lambda n: "%08d" % n)
    shozokumei = factory.Faker("prefecture", locale="ja_jp")
    kakarikouzamei = factory.Faker("city", locale="ja_jp")
    shokumei = factory.Faker("town", locale="ja_jp")
    kanjishimei = factory.Faker("name", locale="ja_jp")
    furigana = factory.Faker("kana_name", locale="ja_jp")
    naisenbangou = factory.Sequence(lambda n: "%04d" % n)
    mail_address = factory.Faker("ascii_safe_email")
