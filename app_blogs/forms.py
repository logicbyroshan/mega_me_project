from django import forms
from django.contrib.auth.models import User
from .models import Subscription  # If you have a Subscription model
from django.contrib.auth.forms import UserCreationForm


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']  # Adjust fields as needed


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
