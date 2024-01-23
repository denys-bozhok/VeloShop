from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now

import uuid
from typing import Any
from datetime import timedelta

from users.models import User, EmailVerification


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
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    def save(self, commit: bool = True) -> Any:
        user = super(UserRegistrationForm, self).save()
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(
            code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()

        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput'}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-imput', 'readonly': True}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-imput', 'readonly': True}))

    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'image-input'}), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image',]
