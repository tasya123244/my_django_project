from django import forms
from django.forms import ModelForm
from .models import AbcModel

class AbcModelForm(ModelForm):
    class Meta:
        model = AbcModel
        fields = ['full_name', 'x', 'y']  
