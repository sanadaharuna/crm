from django import forms


class ApplicationUploadForm(forms.Form):
    file = forms.FileField(label="CSVファイル")

