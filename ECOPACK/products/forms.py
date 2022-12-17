from django.db import models
from django.forms import fields
from .models import Product
from django import forms


class UserImage(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'size', 'layer_field', 'category', 'picture')
