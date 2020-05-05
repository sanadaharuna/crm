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
    q = forms.CharField(label="キーワード検索", required=False)

    def __init__(self, *args, **kwargs):
        super(NayoseSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('q', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            # Submit('submit', '検索'),
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("nayose:list")
        self.helper.add_input(
            Submit('', '検索', css_class='btn btn-primary'))
