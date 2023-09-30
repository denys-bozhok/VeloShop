
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from users.models import CustomUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your e-mail'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your first name'}))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your last name'}))
    
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your phone'}))
    
    email = forms.IntegerField(widget=forms.EmailInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your password'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Confirm your password'}))
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')