from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Nayose


class NayoseForm(forms.ModelForm):
    class Meta:
        model = Nayose
        fields = "__all__"
        widgets = {
            "date_of_birth": DatePickerInput(
                format="%Y-%m-%d",
                options={"locale": "ja", "dayViewHeaderFormat": "YYYY年 MMMM"},
            )
        }


class NayoseSearchForm(forms.Form):
    kanjishimei = forms.CharField(label="漢字氏名", required=False)
    kanashimei = forms.CharField(label="カナ氏名", required=False)
