from django import forms


class BiasForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(attrs={'cols': 150, 'rows': 3}))
