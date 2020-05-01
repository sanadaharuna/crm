from django.db.models import CharField, DateField, IntegerField, Model

from base.common import calculate_age
from base.consts import SEX_CHOICES


class Researcher(Model):
    researcher_id = IntegerField("研究者番号", primary_key=True)
    kanjishimei_sei = CharField("漢字氏名・姓", max_length=255)
    kanjishimei_mei = CharField("漢字氏名・名", max_length=255)
    kanashimei_sei = CharField("カナ氏名・姓", max_length=255)
    kanashimei_mei = CharField("カナ氏名・名", max_length=255)
    date_of_birth = DateField("生年月日")
    sex = CharField("性別", choices=SEX_CHOICES, max_length=1)
    department = CharField("部局名", max_length=255)
    title = CharField("職位", max_length=255)

    @property
    def age(self):
        return calculate_age(self.date_of_birth)

    def __str__(self):
        return self.kanjishimei_sei
