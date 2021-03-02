from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse


class KeywordSearchForm(forms.Form):
    q = forms.CharField(label="キーワード", required=False)

    def __init__(self, *args, **kwargs):
        super(KeywordSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('q', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("work:list")
        self.helper.add_input(
            Submit('', '検索', css_class='btn btn-primary'))
