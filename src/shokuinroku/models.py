from django.db import models


class Shokuin(models.Model):
    as_of = models.DateField("基準日")
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
