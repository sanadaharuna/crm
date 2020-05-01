from django import forms


class ResearcherUploadForm(forms.Form):
    file = forms.FileField(label="CSVファイル")


class ResearcherSearchForm(forms.Form):
    kanjishimei = forms.CharField(label="漢字氏名", required=False)
    kanashimei = forms.CharField(label="カナ氏名", required=False)
