# Generated by Django 3.1.5 on 2021-01-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_estore'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_url',
            field=models.URLField(default='localhost:8000', max_length=500),
        ),
    ]
