from django import forms

class RSVPForm(forms.Form):
    email = forms.EmailField()