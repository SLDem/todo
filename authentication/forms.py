from django import forms
from authentication.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    """Form for signing up users."""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'signup-email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-name'}), label='Username')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'signup-password'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'signup-password'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ('email', 'username', )
