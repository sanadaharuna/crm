from django.db import models
from crm.lib.models import Person


class Project(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "U-goグラント課題"
    nendo = models.IntegerField("年度")
    kadaimei = models.CharField("課題名", max_length=200)
    KUBUN_CHOICES = (("1", "新規"), ("2", "継続"))
    kubun = models.CharField("区分", max_length=1, choices=KUBUN_CHOICES)
    JUDGEMENT_CHOICES = (("1", "採択"), ("2", "不採択"), ("3", "追加採択"))
    saihi = models.CharField("採否", max_length=1, choices=JUDGEMENT_CHOICES)
    kiboukenkyuuhi = models.IntegerField("希望研究費")
    haibunkingaku = models.IntegerField("配分金額")
    bikou = models.CharField("備考", max_length=200)

    def __str__(self):
        return self.kadaimei


class Member(Person):
    class Meta:
        verbose_name = verbose_name_plural = "U-goグラント申請者"
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    shokumei = models.CharField("職名", max_length=50)
    nenrei = models.IntegerField("年齢")
    SEX_CHOICES = (("0", ""), ("1", "男性"), ("2", "女性"), ("9", "その他"))
    seibetsu = models.CharField("性別", choices=SEX_CHOICES, max_length=1)
    ROLE_CHOICES = (("1", "代表"), ("2", "分担"), ("9", "その他"))
    role = models.CharField("役割", max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.eradcode
