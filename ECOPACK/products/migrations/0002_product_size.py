# Generated by Django 4.1.4 on 2022-12-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=3, null=True, verbose_name='Объем'),
        ),
    ]
