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

    def __init__(self, *args, **kwargs):
        super(NayoseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class NayoseSearchForm(forms.Form):
    nayose_id = forms.CharField(label="名寄せID", required=False)
    erad_id = forms.CharField(label="研究者番号", required=False)
    shokuin_id = forms.CharField(label="常勤職員番号", required=False)
    hijoukin_id = forms.CharField(label="非常勤職員番号", required=False)
    kanjishimei = forms.CharField(label="漢字氏名", required=False)
    kanashimei = forms.CharField(label="カナ氏名", required=False)

    def __init__(self, *args, **kwargs):
        super(NayoseSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('nayose_id', css_class='form-group col-md-3 mb-0'),
                Column('erad_id', css_class='form-group col-md-3 mb-0'),
                Column('shokuin_id', css_class='form-group col-md-3 mb-0'),
                Column('hijoukin_id', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('kanjishimei', css_class='form-group col-md-6 mb-0'),
                Column('kanashimei', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("nayose:list")
        self.helper.add_input(
            Submit('', '検索', css_class='btn btn-primary'))
