from django import forms

class InputForm(forms.Form):
    artist = forms.CharField(label='Musical Artist', max_length=225)