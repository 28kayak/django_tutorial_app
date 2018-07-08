from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mial = forms.CharField(label='mail')
    age  = forms.IntegerField(label='age')
