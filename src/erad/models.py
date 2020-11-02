from datetime import date

from django.db import models


class Researcher(models.Model):
    eradcode = models.CharField("研究者番号", max_length=8, primary_key=True)
    kenkyuushashimei_sei = models.CharField("研究者氏名-姓", max_length=50)
    kenkyuushashimei_mei = models.CharField("研究者氏名-名", max_length=50)
    furigana_sei = models.CharField(
        "フリガナ-姓", max_length=50, blank=True, null=True)
    furigana_mei = models.CharField(
        "フリガナ-名", max_length=50,  blank=True, null=True)
    tsuushoumei_sei = models.CharField(
        "通称名-姓", max_length=50,  blank=True, null=True)
    tsuushoumei_mei = models.CharField(
        "通称名-名", max_length=50,  blank=True, null=True)
    tsuushoumeifurigana_sei = models.CharField(
        "通称名フリガナ-姓", max_length=50,  blank=True, null=True)
    tsuushoumeifurigana_mei = models.CharField(
        "通称名フリガナ-名", max_length=50,  blank=True, null=True)
    eiji_sei = models.CharField("英字-姓", max_length=50, blank=True, null=True)
    eiji_mei = models.CharField("英字-名", max_length=50, blank=True, null=True)
    seinengappi = models.DateField("生年月日", blank=True, null=True)
    SEX_CHOICES = (("0", ""), ("1", "男性"), ("2", "女性"), ("9", "その他"))
    seibetsu = models.CharField("性別", choices=SEX_CHOICES, max_length=1)
    gakui = models.CharField("学位", max_length=50,  blank=True, null=True)
    gakuishutokunengappi = models.CharField(
        "学位取得年月日", max_length=50, blank=True, null=True)
    bukyokumei = models.CharField("部局名", max_length=50)
    shokumei = models.CharField("職位", max_length=50)
    mailaddress1 = models.EmailField("メールアドレス1", blank=True, null=True)
    mailaddress2 = models.EmailField("メールアドレス2", blank=True, null=True)
    kakenhiouboshikaku = models.CharField("科研費応募資格", max_length=1)
    shutarukenkyuukikan = models.CharField("主たる研究機関", max_length=1)
    bukyokuchakuninbi = models.DateField("部局着任日", blank=True, null=True)
    bukyokutaininbi = models.DateField("部局退任日", blank=True, null=True)

    def age(self):
        today = date.today()
        age = today.year - self.seinengappi.year
        # 今年の誕生日を迎えていなければ、ageを1つ減らす
        if (today.month, today.day) < (self.seinengappi.month, self.seinengappi.day):
            age -= 1
        return age

    class Meta:
        verbose_name = "研究者データ"
        verbose_name_plural = "研究者データ"


class Application(models.Model):
    kakushu_no = models.CharField("各種No", max_length=20)
    kadai_id = models.CharField("課題ID", max_length=20)
    oubo_saitaku_bangou = models.CharField("応募／採択番号", max_length=20)
    nendo = models.IntegerField("年度")
    seido_code = models.CharField("制度コード", max_length=7)
    seidomei = models.CharField("制度名", max_length=200)
    jigyoumei = models.CharField("事業名", max_length=200)
    koubogroupmei = models.CharField("公募グループ名", max_length=200)
    koubo_nendo = models.IntegerField("公募年度")
    koubomei = models.CharField("公募名", max_length=200)
    kadaimei = models.CharField("研究開発課題名", max_length=200)
    kaishi_nendo = models.IntegerField("研究期間開始年度")
    shuuryou_nendo = models.IntegerField("研究期間終了年度")
    STATUS_CHOICE = (("1", "応募中"), ("2", "応募済"), ("3", "審査中"), ("4", "審査済"),
                     ("5", "採択"), ("6", "不受理"), ("7", "取下げ"), ("8", "不採択（足切り）"), ("9", "不採択"))
    status = models.CharField("ステータス", max_length=1, choices=STATUS_CHOICE)
    eradcode = models.CharField("研究者番号", max_length=8)

    class Meta:
        verbose_name = "応募データ"
        verbose_name_plural = "応募データ"
