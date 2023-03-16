from django import forms
from django.contrib.auth.models import User
from .models import League

class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name',]
        labels = {'name' : 'Name'}