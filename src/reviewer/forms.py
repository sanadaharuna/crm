from django import forms

from .models import Reviewer


class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = "__all__"
        widgets = {"researcher": forms.TextInput()}


class ReviewerSearchForm(forms.Form):
    fiscalyear = forms.CharField(label="年度", required=False)
    committee = forms.CharField(label="委員会", required=False)
    name = forms.CharField(label="氏名", required=False)
    is_awarded = forms.BooleanField(label="表彰", required=False)
