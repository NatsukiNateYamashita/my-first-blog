# Generated by Django 2.2.4 on 2019-08-30 06:31

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_photo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/', verbose_name=blog.models.Photo),
            preserve_default=False,
        ),
    ]
