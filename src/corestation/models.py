from crm.lib.models import Person
from django.db import models


class Station(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "コア・ステーション"

    attached_to = models.CharField("附置組織", max_length=50)
    name = models.CharField("事業体名", max_length=255)
    date_of_establishment = models.DateField("設立年月日")

    def __str__(self):
        return self.name


class Member(Person):
    class Meta:
        verbose_name = verbose_name_plural = "構成員"

    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    specialized_field = models.CharField("専門分野", max_length=200)
    REPRESENTATIVE_CHOICES = (("0", ""), ("1", "事業代表者"),)
    is_representative = models.CharField("事業代表者", choices=REPRESENTATIVE_CHOICES, max_length=1)

    def __str__(self):
        return self.eradcode
