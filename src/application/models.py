from django.db import models


class Application(models.Model):
    nendo = models.IntegerField("年度", blank=True, null=True)
    seido_code = models.CharField("制度コード", max_length=7, blank=True, null=True)
    seidomei = models.CharField("制度名", max_length=200, blank=True, null=True)
    jigyou_code = models.CharField("事業コード", max_length=7, blank=True, null=True)
    jigyoumei = models.CharField("事業名", max_length=200, blank=True, null=True)
    koubogroup_code = models.CharField("公募グループコード", max_length=8, blank=True, null=True)
    koubogroupmei = models.CharField("公募グループ名", max_length=200, blank=True, null=True)
    koubo_code = models.CharField("公募コード", max_length=7, blank=True, null=True)
    koubomei = models.CharField("公募名", max_length=200, blank=True, null=True)
    kenkyuukaihatsukadaimei = models.CharField(
        "研究開発課題名", max_length=200, blank=True, null=True
    )
    gyoumu_main_status = models.IntegerField("業務メインステータス", blank=True, null=True)
    researcher_id = models.CharField("研究者番号", max_length=8, blank=True, null=True)
    shimeikanji_sei = models.CharField("氏名漢字（姓）", max_length=200, blank=True, null=True)
    shimeikanji_mei = models.CharField("氏名漢字（名）", max_length=200, blank=True, null=True)
    kenkyuukikan_code = models.CharField(
        "研究機関コード", max_length=200, blank=True, null=True
    )
    kenkyuukikanmei = models.CharField("研究機関名", max_length=200, blank=True, null=True)
    bukyoku_code = models.CharField("部局コード", max_length=200, blank=True, null=True)
    bukyokumei = models.CharField("部局名", max_length=200, blank=True, null=True)
    shokukai_code = models.CharField("職階コード", max_length=200, blank=True, null=True)
    yakushoku = models.CharField("役職", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.koubomei

