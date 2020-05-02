from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Kaken


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
        }


class KakenSearchForm(forms.Form):
    fiscalyear = forms.CharField(label="支援年度", required=False)
    tantousha = forms.CharField(label="担当（主・副）", required=False)
