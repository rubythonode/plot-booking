# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0004_auto_20160713_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saletransaction',
            name='emi_txn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_transaction_emi', to='accounts_api.EMI_schedule'),
        ),
    ]