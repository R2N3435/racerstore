# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20161221_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='mobile',
            new_name='mobile_number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address2',
            new_name='secondary_address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='mobile2',
            new_name='secondary_mobile_number',
        ),
    ]
