from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse


class ResearcherSearchForm(forms.Form):
    q = forms.CharField(label="e-Rad研究者データから検索", required=False)

    def __init__(self, *args, **kwargs):
        super(ResearcherSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('q', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("erad:list")
        self.helper.add_input(
            Submit('', '検索', css_class='btn btn-primary'))
