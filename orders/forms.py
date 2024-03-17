from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    owner_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    owner_surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    adress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adress'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    
    class Meta:
        model = Order
        fields = ('owner_name', 'owner_surname', 'email', 'adress', 'city',)