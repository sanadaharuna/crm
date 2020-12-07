from crm.lib.models import Person
from django.db import models


class Attribute(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "属性"

    zokusei = models.CharField("属性", max_length=50)

    def __str__(self):
        return self.attribute


class Eligible(Person):
    class Meta:
        verbose_name = verbose_name_plural = "対象者"

    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    nendo = models.IntegerField("実施年度")
    bikou = models.CharField("備考", max_length=200)

    def __str__(self):
        return self.eradcode
