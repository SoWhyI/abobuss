from django.db import models
from users.models import CustomUser
from django.shortcuts import reverse


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=False)
    product_list = models.JSONField(unique=False)
