# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-01 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20170101_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Cart')),
                ('recomm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.games')),
            ],
        ),
    ]
