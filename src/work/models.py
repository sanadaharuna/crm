from django.db import models


class Member(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "参画研究者"
    eradcode = models.CharField("研究者番号", max_length=8)
    ROLE_CHOICES = (("1", "代表"), ("2", "分担"), ("3", "筆頭著者"), ("4", "責任著者"))
    role = models.CharField("役割", max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.eradcode


class Keyword(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "キーワード"
    keyword = models.CharField("キーワード", max_length=255)

    def __str__(self):
        return self.keyword_id


class Work(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "研究業績"
    SOURCE_CHOICES = (("1", "KAKEN"), ("2", "JSTDB"), ("3", "WoS"))
    source = models.CharField("取得元", max_length=1, choices=SOURCE_CHOICES)
    pid = models.CharField("永続的識別子", max_length=255, primary_key=True)
    category = models.CharField("種別", max_length=255)
    title = models.CharField("タイトル", max_length=255)
    year = models.IntegerField("開始年度／公表年")
    members = models.ManyToManyField(Member)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.unique_id
