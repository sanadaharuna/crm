from django.db import models
from researcher.models import Researcher


class Promotion(models.Model):
    title = models.CharField("施策名", max_length=200)
    fiscalyear = models.IntegerField("年度")

    def __str__(self):
        return self.title + " " + str(self.fiscalyear)


class Candidate(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)
    researcher = models.ForeignKey(
        Researcher,
        verbose_name="研究者番号",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    name = models.CharField("氏名", max_length=200)
    affiliation = models.CharField("所属", max_length=200)
    judgement = models.BooleanField("審査結果", blank=True, null=True)

    def __str__(self):
        return self.name

