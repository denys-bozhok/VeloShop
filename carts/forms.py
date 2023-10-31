from django import forms

from . import models


class EditProductSumForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        exclude = ('quantity',)