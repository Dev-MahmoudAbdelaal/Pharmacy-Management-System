from dataclasses import fields
from django import forms
from .models import drugs

class drugsform(forms.ModelForm):
    class Meta:
        model = drugs
        fields = '__all__'
