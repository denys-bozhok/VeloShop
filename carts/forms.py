from . import models
from django import forms

from .models import Cart


class QuantityUpdateView(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-imput', }))

    class Meta:
        model = Cart
        exclude = ['quantity',]
