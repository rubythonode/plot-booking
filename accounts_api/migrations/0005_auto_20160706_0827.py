# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0004_emi_duration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EMI_transactions',
            new_name='EMI_schedule',
        ),
    ]
