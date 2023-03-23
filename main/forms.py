from django import forms
from django.contrib.auth.models import User
from .models import League, Team, Match, Player

class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name',]
        labels = {'name' : 'Name'}

class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'shorthand']

class CreatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'second_name', 'position']

class EditMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team_result', 'away_team_result']
        labels = {'home_team_result' : 'Home team result', 'away_team_result' : 'Away team result'}