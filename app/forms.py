from django import forms
from .models import PlayerTeams


class PlayerTeamsForm(forms.Form):
    player_teams = forms.ModelChoiceField(
        queryset=PlayerTeams.objects.all(), label="Select Team"
    )
