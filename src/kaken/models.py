from django.db import models

from base import consts
# from researcher.models import Researcher
from nayose.models import Nayose


class Support(models.Model):
    nayose = models.ForeignKey(
        Nayose,
        verbose_name="名寄せID",
        on_delete=models.PROTECT,
    )
    name = models.CharField("氏名", max_length=200)
    affiliation = models.CharField("所属", max_length=200)
    shutantou = models.CharField("主担当", max_length=200, blank=True, null=True)
    fukutantou = models.CharField("副担当", max_length=200, blank=True, null=True)
    # fiscalyear = models.IntegerField("年度")
    date_received = models.DateField("受付日")
    # date_completed = models.DateField("完了日", blank=True, null=True)

    class Meta:
        abstract = True


class Category(models.Model):
    code = models.IntegerField("研究種目コード", primary_key=True)
    name = models.CharField("研究種目名", max_length=200)

    def __str__(self):
        return self.name


class SupportType(models.Model):
    code = models.IntegerField("支援種類コード", primary_key=True)
    name = models.CharField("支援種類名", max_length=200)

    def __str__(self):
        return self.name


class Kaken(Support):
    category = models.ForeignKey(
        Category, verbose_name="研究種目", on_delete=models.PROTECT
    )
    support_type = models.ForeignKey(
        SupportType, verbose_name="支援種別", on_delete=models.PROTECT
    )
    judgement = models.IntegerField(
        "審査結果", choices=consts.JUDGEMENT_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.name
