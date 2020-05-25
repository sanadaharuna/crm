from datetime import date
from django.db import models


class Nayose(models.Model):
    nayose_id = models.AutoField("名寄せID", primary_key=True)
    erad_id = models.CharField(
        "研究者番号", max_length=8, blank=True, null=True, unique=True)
    shokuin_id = models.CharField(
        "職員番号（常勤）", max_length=8, blank=True, null=True, unique=True)
    hijoukin_id = models.CharField(
        "職員番号（非常勤）", max_length=8, blank=True, null=True, unique=True)
    kanjishimei_sei = models.CharField("漢字氏名（姓）", max_length=30)
    kanjishimei_mei = models.CharField("漢字氏名（名）", max_length=30)
    kanashimei_sei = models.CharField("カナ氏名（姓）", max_length=30)
    kanashimei_mei = models.CharField("カナ氏名（名）", max_length=30)
    date_of_birth = models.DateField("生年月日")
    SEX_CHOICES = (("0", ""), ("1", "男性"), ("2", "女性"), ("9", "その他"))
    sex = models.CharField("性別", choices=SEX_CHOICES, max_length=1)

    def __str__(self):
        return self.kanjishimei_sei + self.kanjishimei_mei

    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        # 今年の誕生日を迎えていなければ、ageを1つ減らす
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


class Shokuin(models.Model):
    kijunbi = models.DateField("基準日")
    shokuin_id = models.CharField("職員番号", max_length=8)
    shozokumei = models.CharField("所属名", max_length=50)
    kakarikouzamei = models.CharField("係講座名", max_length=50, blank=True)
    shokumei = models.CharField("職名", max_length=50, blank=True)
    kanjishimei = models.CharField("漢字氏名", max_length=50)
    furigana = models.CharField("フリガナ", max_length=50)
    naisenbangou = models.CharField("内線番号", max_length=10, blank=True)
    mail_address = models.EmailField("メールアドレス", blank=True)

    def __str__(self):
        return self.kanjishimei


class Erad(models.Model):
    kijunbi = models.DateField("基準日")
    eradcode = models.CharField("研究者番号", max_length=8)
    kanjishimei_sei = models.CharField("漢字氏名・姓", max_length=50)
    kanjishimei_mei = models.CharField("漢字氏名・名", max_length=50)
    kanashimei_sei = models.CharField("カナ氏名・姓", max_length=50)
    kanashimei_mei = models.CharField("カナ氏名・名", max_length=50)
    date_of_birth = models.DateField("生年月日")
    sex = models.CharField("性別", max_length=1)
    department = models.CharField("部局名", max_length=50)
    title = models.CharField("職位", max_length=50)

    def __str__(self):
        return self.kanjishimei_sei + self.kanjishimei_mei
