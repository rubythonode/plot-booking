# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='is_emi_enabled',
            field=models.BooleanField(default=False),
        ),
    ]