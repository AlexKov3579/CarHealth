import re
from django import forms


class NewCarForm(forms.Form):
    manufacturer = forms.CharField(required=True)
    model = forms.CharField(required=True)
    engineType = forms.CharField(required=True)
    engineVol = forms.CharField(required=True)
    year = forms.IntegerField(required=True)
    widgets = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'placeholder': '2020-01-01',
               'type': 'date',
               'value': '2020-01-01',
               'is_required': True
              }) 

    lastCheck = forms.DateField(widget= widgets, required=True)
    nextCheck = forms.DateField(required=True, widget= widgets )
    kilometrage = forms.IntegerField(required=True)

class UpdatePartForm(forms.Form):
    newValue = forms.FloatField()
    partId = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    carId = forms.IntegerField(widget=forms.HiddenInput())
    updateAll = forms.IntegerField(widget=forms.HiddenInput())

