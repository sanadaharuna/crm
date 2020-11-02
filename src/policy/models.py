from crm.lib.models import Person
from django.db import models


class Policy(models.Model):
    shisakumei = models.CharField("施策名", max_length=50)

    class Meta:
        verbose_name = "研究推進施策"
        verbose_name_plural = "研究推進施策"


class Participant(Person):
    policy = models.ForeignKey(Policy, on_delete=models.PROTECT)
    nendo = models.IntegerField("実施年度")
    bikou = models.CharField("備考", max_length=200)

    class Meta:
        verbose_name = "対象者"
        verbose_name_plural = "対象者"
