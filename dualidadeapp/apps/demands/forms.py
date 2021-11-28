from django import forms
from .models import Demand

class DemandForm(forms.ModelForm):

    class Meta:
        model = Demand
        exclude = ('created_on' , 'updated_on',)