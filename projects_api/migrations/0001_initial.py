# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
                ('description', models.CharField(blank=True, max_length=254)),
                ('address', models.TextField(blank=True, max_length=254)),
                ('area', models.CharField(blank=True, max_length=254)),
                ('plot_no', models.CharField(blank=True, max_length=254)),
                ('gat_no', models.CharField(blank=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]