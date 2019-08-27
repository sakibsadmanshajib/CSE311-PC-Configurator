from django import forms

class AddPC(forms.Form):
    cpu = forms.IntegerField()
    ram = forms.IntegerField()
    gpu = forms.IntegerField()
    motherboard = forms.IntegerField()
    storage = forms.IntegerField()