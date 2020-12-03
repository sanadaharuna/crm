from crm.lib.models import Person
from django.db import models


class Policy(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "研究推進施策"

    shisakumei = models.CharField("施策名", max_length=50)

    def __str__(self):
        return self.shisakumei


class Participant(Person):
    class Meta:
        verbose_name = verbose_name_plural = "対象者"

    policy = models.ForeignKey(Policy, on_delete=models.PROTECT)
    nendo = models.IntegerField("実施年度")
    bikou = models.CharField("備考", max_length=200)

    def __str__(self):
        return self.eradcode
