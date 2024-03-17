from . import models
from django import forms

from .models import Cart


class CartQuantityUpdateForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['quantity',]
