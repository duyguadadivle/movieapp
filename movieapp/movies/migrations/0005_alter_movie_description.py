# Generated by Django 4.0.3 on 2022-05-05 10:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_image_cover_alter_movie_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]