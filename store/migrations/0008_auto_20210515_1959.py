# Generated by Django 3.1.5 on 2021-05-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estore',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]