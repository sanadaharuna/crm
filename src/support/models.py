from django.db import models

from crm.lib.models import Person

JUDGEMENT_CHOICES = (("0", ""), ("1", "採択"), ("2", "不採択"), ("9", "応募なし"))


class Support(Person):
    class Meta:
        abstract = True

    nendo = models.IntegerField("年度")
    uketsukebi = models.DateField("受付日")
    kanryoubi = models.DateField("完了日", blank=True, null=True)
    shutantou = models.CharField("主担当", max_length=50, blank=True, null=True)
    fukutantou = models.CharField("副担当", max_length=50, blank=True, null=True)


class Kakenhi(Support):
    class Meta:
        verbose_name = verbose_name_plural = "科研費申請書添削"

    shumoku = models.CharField("研究種目", max_length=50, blank=True)
    saihi = models.CharField("採否", max_length=1, choices=JUDGEMENT_CHOICES)
    bikou = models.CharField("備考", max_length=200, blank=True)

    def __str__(self):
        return self.eradcode


class CompetitiveFund(Support):
    class Meta:
        verbose_name = verbose_name_plural = "競争的研究資金申請支援"

    haibunkikan = models.CharField("配分機関", max_length=50)
    koubomei = models.CharField("公募名", max_length=200)
    saihi = models.CharField("採否", max_length=1, choices=JUDGEMENT_CHOICES)

    def __str__(self):
        return self.eradcode


class Matching(Support):
    class Meta:
        verbose_name = verbose_name_plural = "マッチング支援"

    def __str__(self):
        return self.eradcode
