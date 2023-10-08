
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your e-mail'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your username'}))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your first name'}))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your last name'}))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Enter your password'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-imput',
        'placeholder': 'Confirm your password'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput'}))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput'}))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput', 'readonly': True}))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-imput', 'readonly': True}))
    
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file'}), required=False)
    
    # print(image)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']