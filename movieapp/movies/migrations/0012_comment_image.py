# Generated by Django 4.0.3 on 2022-05-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_slider_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to='person'),
        ),
    ]
