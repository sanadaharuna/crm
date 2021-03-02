from django.db import models


class Keyword(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "キーワード"
    # keyword_id = models.IntegerField("キーワードID", primary_key=True)
    keyword = models.CharField("キーワード", max_length=255)
    researcher_count = models.IntegerField("使用研究者数")
    cumcount = models.IntegerField("のべ使用回数")

    def __str__(self):
        return self.keyword


class Work(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "研究課題"
    awardnumber = models.CharField("課題番号", max_length=255)
    title = models.CharField("課題名", max_length=255)
    startfiscalyear = models.IntegerField("研究開始年度")
    role = models.CharField("役割", max_length=255)
    category_name = models.CharField("研究種目", max_length=255)
    eradcode = models.CharField("研究者番号", max_length=8)
    fullname = models.CharField("氏名", max_length=255)
    institution = models.CharField("部局名", max_length=255)
    department = models.CharField("部局名", max_length=255)
    jobtitle = models.CharField("職名", max_length=255)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.eradcode
