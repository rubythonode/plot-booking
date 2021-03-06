# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import plots.lib.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_api', '0004_auto_20160703_0530'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now)),
                ('total_amount', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('paid_amount', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('intrest_rate', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('total_intrest', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('paid_status', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EMI_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now)),
                ('emi_schedule_date', models.DateField(null=True)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('paid_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_emi_enabled', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now)),
                ('sale_completed', models.BooleanField(default=False)),
                ('basic_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('sales_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('remaning_cost', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='SaleTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('trasaction_type', models.CharField(blank=True, max_length=254)),
                ('trasaction_type_no', models.CharField(blank=True, max_length=254)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('is_emi', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('emi_txn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_transaction_emi', to='accounts_api.EMI_schedule')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_transaction_sale', to='customer_api.Customer')),
            ],
        ),
    ]
