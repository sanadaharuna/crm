from django.db import models

from nayose.models import Nayose


class Support(models.Model):
    date_received = models.DateField("受付日")
    nayose = models.ForeignKey(
        Nayose,
        verbose_name="名寄せID",
        on_delete=models.PROTECT,
    )
    name = models.CharField("氏名", max_length=50)
    affiliation = models.CharField("所属", max_length=50)
    shutantou = models.CharField("主担当", max_length=50, blank=True, null=True)
    fukutantou = models.CharField("副担当", max_length=50, blank=True, null=True)
    remarks = models.CharField("備考", max_length=250, blank=True, null=True)

    class Meta:
        abstract = True
