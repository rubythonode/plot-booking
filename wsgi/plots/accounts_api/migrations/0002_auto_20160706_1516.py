# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_api', '0001_initial'),
        ('customer_api', '0004_auto_20160703_0530'),
        ('booking_api', '0001_initial'),
        ('projects_api', '0013_project_village'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_booking', to='booking_api.Booking'),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_customer', to='customer_api.Customer'),
        ),
        migrations.AddField(
            model_name='sale',
            name='plot_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_plots', to='projects_api.Plots'),
        ),
        migrations.AddField(
            model_name='emi_schedule',
            name='emi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emi_data', to='accounts_api.EMI'),
        ),
        migrations.AddField(
            model_name='emi',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emi_sale', to='accounts_api.Sale'),
        ),
    ]