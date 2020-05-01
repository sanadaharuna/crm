from django.db import models

# from researcher.models import Researcher
from nayose.models import Nayose


class Reviewer(models.Model):
    fiscalyear = models.IntegerField("年度")
    committee = models.CharField("委員会", max_length=200)
    # nayose = models.ForeignKey(
    #     Nayose, verbose_name="研究者番号", on_delete=models.PROTECT, blank=True, null=True
    # )
    nayose_id = models.IntegerField("研究者番号", blank=True, null=True)
    name = models.CharField("氏名", max_length=200)
    affiliation = models.CharField("所属", max_length=200)
    is_awarded = models.BooleanField("表彰", blank=True, null=True)
