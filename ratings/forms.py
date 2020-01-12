from django import forms
from .models import Profile,Project

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['editor','profile','pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['editor']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
