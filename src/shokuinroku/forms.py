from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse

from .models import Shokuin


def get_choices():
    qs = Shokuin.objects.values_list("as_of", flat=True).distinct()
    choices = [(dt.strftime("%Y-%m-%d"), dt.strftime("%Y-%m-%d")) for dt in qs]
    choices = tuple(choices)
    return choices


class ShokuinSearchForm(forms.Form):
    q = forms.ChoiceField(choices=get_choices,
                          label="基準日", widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(ShokuinSearchForm, self).__init__(*args, **kwargs)
        # FormHelper
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('q', css_class='form-group col-md-3 mb-0'),
                # css_class='form-row'
            ),
        )
        self.helper.form_method = "GET"
        self.helper.form_action = reverse("shokuinroku:list")
        self.helper.add_input(
            Submit('', '検索', css_class='btn btn-primary'))
