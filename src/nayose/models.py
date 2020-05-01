from django.db import models

from base.consts import SEX_CHOICES


class Nayose(models.Model):
    nayose_id = models.AutoField("名寄せID", primary_key=True)
    erad_id = models.CharField("研究者番号", max_length=8, blank=True, null=True)
    shokuin_id = models.CharField("職員番号", max_length=8, blank=True, null=True)
    hijoukin_id = models.CharField(
        "非常勤職員番号", max_length=8, blank=True, null=True)
    kanjishimei_sei = models.CharField("漢字氏名・姓", max_length=255)
    kanjishimei_mei = models.CharField("漢字氏名・名", max_length=255)
    kanashimei_sei = models.CharField("カナ氏名・姓", max_length=255)
    kanashimei_mei = models.CharField("カナ氏名・名", max_length=255)
    date_of_birth = models.DateField("生年月日")
    sex = models.CharField("性別", choices=SEX_CHOICES, max_length=1)

    def __str__(self):
        return self.id + " : " + self.kanjishimei_sei + " " + self.kanjishimei_mei
