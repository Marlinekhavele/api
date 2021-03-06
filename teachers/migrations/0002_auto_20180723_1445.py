# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countyofficer',
            name='is_countyofficer',
            field=models.BooleanField(default=True, verbose_name='countyofficer status'),
        ),
        migrations.AlterField(
            model_name='headteacher',
            name='is_headteacher',
            field=models.BooleanField(default=True, verbose_name='headteacher status'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=True, verbose_name='teacher status'),
        ),
    ]
