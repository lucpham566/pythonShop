from django import forms

class SendCheckout(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'title'}))
    email = forms.EmailField()
    phone = forms.CharField(widget=forms.Textarea(attrs={'class': 'content'}))
    address = forms.TextInput()