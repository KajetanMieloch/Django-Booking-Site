from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'Kajetan.Mieloch2002',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'Password123.',
        }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'Kajetan.Mieloch2002',
        }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'example@example.com',
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'Password123.',
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-4 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline',
        'placeholder': 'Password123.',
        }))