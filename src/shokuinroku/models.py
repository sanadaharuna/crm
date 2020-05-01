from django.db.models import CharField, EmailField, IntegerField, Model


class Shokuin(Model):
    shokuin_id = IntegerField("職員番号", primary_key=True)
    shozokumei = CharField("所属名", max_length=255)
    kakarikouzamei = CharField("係講座名", max_length=255, blank=True)
    shokumei = CharField("職名", max_length=200, blank=True)
    kanjishimei = CharField("漢字氏名", max_length=255)
    furigana = CharField("フリガナ", max_length=255)
    naisenbangou = CharField("内線番号", max_length=255, blank=True)
    mail_address = EmailField("メールアドレス", max_length=255, blank=True)

    def __str__(self):
        return self.kanjishimei
