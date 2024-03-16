from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    owner_name = forms.CharField(max_length=32)
    owner_surname = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)
    adress = forms.CharField(max_length=256)
    
    class Meta:
        model = Order
        fields = ('owner_name', 'owner_surname', 'email', 'adress', )