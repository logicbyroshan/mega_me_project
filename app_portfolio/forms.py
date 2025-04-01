from django import forms
from .models import Subscription  # If you have a Subscription model

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']  # Adjust fields as needed
