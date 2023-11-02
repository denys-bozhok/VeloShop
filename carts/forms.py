from django import forms

from . import models


class EditProductSumForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-imput'}))
    class Meta:
        model = models.Cart
        exclude = ['quantity',]