from django import forms

from .models import Candidate, Promotion


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__"
        # widgets = {
        #     # "title": forms.TextInput(),
        #     # "fiscalyear": forms.TextInput(),
        # }


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        widgets = {
            # "program": forms.TextInput(),
            "researcher": forms.TextInput(),
            # "name": forms.TextInput(),
            # "affiliation": forms.TextInput(),
        }


class PromotionSearchForm(forms.Form):
    fiscalyear = forms.CharField(label="実施年度", required=False)
    title = forms.CharField(label="施策名", required=False)

