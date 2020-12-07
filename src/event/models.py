from django.db import models
from crm.lib.models import Person


class Event(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "イベント"

    title = models.CharField("催事名", max_length=200)
    venue = models.CharField("会場", max_length=50)
    kaisaibi = models.DateField("開催日")
    nendo = models.IntegerField("開催年度")

    def __str__(self):
        return self.title


class Attendee(Person):
    class Meta:
        verbose_name = verbose_name_plural = "参加者"

    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    PRESENTER_CHOICES = (("0", ""), ("1", "発表"),)
    is_presenter = models.CharField(
        "発表", choices=PRESENTER_CHOICES, max_length=1)

    def __str__(self):
        return self.eradcode
