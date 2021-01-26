from django.db import models


class Person(models.Model):
    eradcode = models.CharField("研究者番号", max_length=8, blank=True, null=True)
    shimei = models.CharField("氏名", max_length=50, blank=True, null=True)
    shozoku = models.CharField("所属", max_length=50, blank=True, null=True)
    shokui = models.CharField("職位", max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
