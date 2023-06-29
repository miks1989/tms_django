from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=20)
    lastname = forms.CharField(min_length=5, max_length=20)
    age = forms.IntegerField(min_value=0, max_value=99)
