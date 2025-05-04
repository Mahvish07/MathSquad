from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['user_name', 'email', 'contest']
        widgets = {
            'contest': forms.HiddenInput()  # Hide the contest field in the form
        }