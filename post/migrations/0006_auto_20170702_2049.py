# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170629_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=40),
        ),
    ]
