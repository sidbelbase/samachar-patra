from django import forms
from .models import SubscriptionEmail


class SubscriptionForm(forms.Form):
    # modify the attributes to better comply the template used from the template sites
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'id': False,
            'placeholder': 'Enter your email'}))

    class Meta:
        model = SubscriptionEmail
        fields = ['email']
