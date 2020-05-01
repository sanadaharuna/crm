from django import forms


class ShokuinUploadForm(forms.Form):
    file = forms.FileField(label="CSVファイル")
