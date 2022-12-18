from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django import forms
from users.models import CustomUser


class Product_in_cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=False)
    products = models.JSONField(unique=False, null=True)



    def get_absolute_url(self):
        return reverse('list_of_products')
