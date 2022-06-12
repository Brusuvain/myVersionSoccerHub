from dataclasses import field
from django import forms
from .models import Credentials,Teams,Player

class CredentialsForm(forms.ModelForm):
    class Meta:
        model = Credentials
        fields ="__all__"

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields ="__all__"

class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields ="__all__"