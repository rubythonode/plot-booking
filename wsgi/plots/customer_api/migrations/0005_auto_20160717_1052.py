# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import plots.lib.utils


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0004_auto_20160703_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now),
        ),
    ]
