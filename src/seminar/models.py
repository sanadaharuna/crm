from django.db import models
from researcher.models import Researcher


class Seminar(models.Model):
    title = models.CharField("催事名", max_length=200)
    venue = models.CharField("会場", max_length=200)
    date = models.DateField("開催日")
    fiscalyear = models.IntegerField("開催年度")

    def __str__(self):
        return self.title


class Attendance(models.Model):
    seminar = models.ForeignKey(
        Seminar, on_delete=models.PROTECT, verbose_name="催事番号")
    researcher = models.ForeignKey(
        Researcher,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="研究者番号",
    )
    name = models.CharField("氏名", max_length=200, blank=True, null=True)
    affiliation = models.CharField("所属", max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class Attendee(Attendance):
    pass

    def __str__(self):
        return self.name


class Lecturer(Attendance):
    pass

    def __str__(self):
        return self.name
