from django import forms

class PlayerForm(forms.Form):
    tag = forms.CharField(label='Your Player Tag', max_length=12)
