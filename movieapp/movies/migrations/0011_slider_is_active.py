# Generated by Django 4.0.3 on 2022-05-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_remove_slider_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]