from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Kaken, SupportType
from base import consts


class KakenForm(forms.ModelForm):
    class Meta:
        model = Kaken
        fields = "__all__"
        widgets = {
            "researcher": forms.TextInput(),
            "date_received": DatePickerInput(
                format="%Y-%m-%d",
                options={"locale": "ja", "dayViewHeaderFormat": "YYYY年 MMMM"},
            ),
            "date_completed": DatePickerInput(
                format="%Y-%m-%d",
                options={"locale": "ja", "dayViewHeaderFormat": "YYYY年 MMMM"},
            ),
        }


class KakenSearchForm(forms.Form):
    fiscalyear = forms.CharField(label="支援年度", required=False)
    support_type = forms.ModelChoiceField(
        SupportType.objects, label="支援種別", required=False
    )
    tantousha = forms.CharField(label="担当（主・副）", required=False)
    in_progress = forms.BooleanField(label="仕掛中（未完了）の案件のみ表示", required=False)
