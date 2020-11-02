from django.db import models
from crm.lib.models import Person


class Seminar(models.Model):
    title = models.CharField("催事名", max_length=200)
    venue = models.CharField("会場", max_length=50)
    kaisaibi = models.DateField("開催日")
    nendo = models.IntegerField("開催年度")

    class Meta:
        verbose_name = "セミナー"
        verbose_name_plural = "セミナー"


class Attendance(Person):
    seminar = models.ForeignKey(Seminar, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Attendee(Attendance):
    pass

    class Meta:
        verbose_name = "セミナー出席者"
        verbose_name_plural = "セミナー出席者"


class Lecturer(Attendance):
    pass
    class Meta:
        verbose_name = "セミナー講師"
        verbose_name_plural = "セミナー講師"

