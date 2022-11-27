from django import forms
from .models import To_do
from dataclasses import fields

class TodoForm(forms.ModelForm):
    class Meta:
        model=To_do
        fields=('Task','Status')
