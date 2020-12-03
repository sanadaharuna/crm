from django.db import models
from crm.lib.models import Person


class Seminar(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "セミナー"

    title = models.CharField("催事名", max_length=200)
    venue = models.CharField("会場", max_length=50)
    kaisaibi = models.DateField("開催日")
    nendo = models.IntegerField("開催年度")

    def __str__(self):
        return self.title


class Attendance(Person):
    class Meta:
        abstract = True

    seminar = models.ForeignKey(Seminar, on_delete=models.PROTECT)


class Attendee(Attendance):
    class Meta:
        verbose_name = verbose_name_plural = "セミナー出席者"

    def __str__(self):
        return self.eradcode


class Lecturer(Attendance):

    class Meta:
        verbose_name = verbose_name_plural = "セミナー講師"

    def __str__(self):
        return self.eradcode
