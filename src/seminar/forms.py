from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Attendance, Attendee, Lecturer, Seminar


class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = "__all__"
        widgets = {
            "date": DatePickerInput(
                format="%Y-%m-%d",
                options={"locale": "ja", "dayViewHeaderFormat": "YYYY年 MMMM"},
            )
        }


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = "__all__"
        widgets = {"seminar": forms.TextInput(), "researcher": forms.TextInput()}


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = "__all__"
        widgets = {"seminar": forms.TextInput(), "researcher": forms.TextInput()}


class SeminarSearchForm(forms.Form):
    fiscalyear = forms.CharField(label="実施年度", required=False)
    title = forms.CharField(label="催事名", required=False)
    venue = forms.CharField(label="会場", required=False)
