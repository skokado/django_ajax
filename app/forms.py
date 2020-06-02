from django import forms


class GreetForm(forms.Form):
    name = forms.CharField(label='あなたの名前は？')
