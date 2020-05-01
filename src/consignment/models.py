from django.db import models

from kaken.models import Support
from base import consts


class Consignment(Support):
    public_offering = models.IntegerField("公募ID", blank=True, null=True)
    schedule_shomen = models.CharField("書面審査時期", max_length=50, blank=True, null=True)
    schedule_mensetsu = models.CharField("面接審査時期", max_length=50, blank=True, null=True)
    call_for_application = models.CharField(
        "公募名", max_length=200, blank=True, null=True
    )
    funding_agency = models.CharField("配分機関", max_length=50, blank=True, null=True)
    judgement = models.IntegerField(
        "審査結果", choices=consts.JUDGEMENT_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.funding_agency + " / " + self.call_for_application
