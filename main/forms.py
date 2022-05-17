from django import forms

class NewCarForm(forms.Form):
    manufacturer = forms.CharField()
    model = forms.CharField()
    engineType = forms.CharField()
    engineVol = forms.CharField()
    year = forms.IntegerField()
