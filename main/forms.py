from django import forms

class NewCarForm(forms.Form):
    manufacturer = forms.CharField()
    model = forms.CharField()
    engineType = forms.CharField()
    engineVol = forms.CharField()
    year = forms.IntegerField()
    lastCheck = forms.DateField()
    nextCheck = forms.DateField()
    kilometrage = forms.IntegerField()

class UpdatePartForm(forms.Form):
    newValue = forms.FloatField()
    partId = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    carId = forms.IntegerField(widget=forms.HiddenInput())
    updateAll = forms.IntegerField(widget=forms.HiddenInput())

