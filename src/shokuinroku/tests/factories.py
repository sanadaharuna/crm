import factory
import factory.fuzzy
import factory.django
from shokuinroku.models import Shokuin


class ShokuinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shokuin

    as_of = factory.Faker("date")
    shokuin_id = factory.Sequence(lambda n: "%08d" % n)
    shozokumei = factory.Faker("prefecture", locale="ja_jp")
    kakarikouzamei = factory.Faker("city", locale="ja_jp")
    shokumei = factory.Faker("town", locale="ja_jp")
    kanjishimei = factory.Faker("name", locale="ja_jp")
    furigana = factory.Faker("kana_name", locale="ja_jp")
    naisenbangou = factory.Sequence(lambda n: "%04d" % n)
    mail_address = factory.Faker("ascii_safe_email")
