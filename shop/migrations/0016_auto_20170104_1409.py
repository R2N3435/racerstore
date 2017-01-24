# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20170101_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='mouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouse_name', models.CharField(max_length=100)),
                ('mouse_description', models.TextField(max_length=10000)),
                ('mouse_logo', models.FileField(upload_to=b'')),
                ('mouse_company', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('laser', models.BooleanField()),
                ('custom_weight', models.BooleanField()),
                ('extra_keys', models.BooleanField()),
                ('custom_dpi', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommend_mouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomend_mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.mouse')),
            ],
        ),
        migrations.RenameModel(
            old_name='Recommend',
            new_name='Recommend_game',
        ),
        migrations.RenameField(
            model_name='recommend_game',
            old_name='recomend',
            new_name='recomend_game',
        ),
    ]
