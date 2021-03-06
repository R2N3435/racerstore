# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('game_description', models.CharField(max_length=1000)),
                ('game_logo', models.FileField(upload_to=b'')),
                ('game_developers', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
