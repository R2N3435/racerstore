# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-24 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20161222_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='arcade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='bike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='car',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='dirt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='road',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='simulator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='games',
            name='truck',
            field=models.BooleanField(default=False),
        ),
    ]
