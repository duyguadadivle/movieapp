# Generated by Django 4.0.3 on 2022-05-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_person_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_cover',
            field=models.ImageField(upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.ImageField(upload_to='movies'),
        ),
    ]