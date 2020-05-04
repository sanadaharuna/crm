from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse
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

    def __init__(self, *args, **kwargs):
        super(NayoseSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('kanjishimei', css_class='form-group col-md-6 mb-0'),
                Column('kanashimei', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '検索')
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("nayose:list")
