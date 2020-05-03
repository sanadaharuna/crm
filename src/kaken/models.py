from django.db import models

from base import consts
from base.models import Support


class Category(models.Model):
    code = models.IntegerField("研究種目コード", primary_key=True)
    name = models.CharField("研究種目名", max_length=200)

    def __str__(self):
        return self.name


class Kaken(Support):
    category = models.ForeignKey(
        Category, verbose_name="研究種目", on_delete=models.PROTECT
    )
    judgement = models.IntegerField("結果", choices=consts.JUDGEMENT_CHOICES)

    def __str__(self):
        return self.name
