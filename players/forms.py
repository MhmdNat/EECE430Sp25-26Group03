from django import forms
from django.utils import timezone

from .models import VoleyPlayer


class VoleyPlayerForm(forms.ModelForm):
    class Meta:
        model = VoleyPlayer
        fields = ["name", "dateJoined", "position", "salary", "contactPerson"]
        widgets = {
            "dateJoined": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")
        if salary is None:
            raise forms.ValidationError("Salary is required.")
        if salary <= 0:
            raise forms.ValidationError("Salary must be greater than 0.")
        return salary

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit date picker in browser to today or earlier.
        self.fields["dateJoined"].widget.attrs["max"] = timezone.localdate().isoformat()

    def clean_dateJoined(self):
        date_joined = self.cleaned_data.get("dateJoined")
        if date_joined and date_joined > timezone.localdate():
            raise forms.ValidationError("Date joined cannot be in the future.")
        return date_joined
