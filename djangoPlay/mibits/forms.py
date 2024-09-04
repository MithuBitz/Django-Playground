from django import forms
from .models import NamesList

class NameListForm(forms.Form):
    name_list = forms.ModelChoiceField(queryset=NamesList.objects.all(), label="Select Names")
