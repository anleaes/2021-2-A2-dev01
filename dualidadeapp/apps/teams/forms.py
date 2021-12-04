from django import forms
from .models import Team

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        exclude = ('created_on' , 'updated_on',)
