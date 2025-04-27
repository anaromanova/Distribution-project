from django import forms
from .models import Distribution

class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ['start_time', 'end_time', 'status', 'message', 'recipients']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'recipients': forms.CheckboxSelectMultiple(),
        }
