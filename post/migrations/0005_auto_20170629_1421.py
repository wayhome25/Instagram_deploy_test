# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 05:21
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170628_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to=post.models.photo_path),
        ),
    ]
