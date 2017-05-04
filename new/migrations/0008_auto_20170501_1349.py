# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_auto_20170501_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercost',
            name='unit_cost',
            field=models.PositiveIntegerField(default=500),
        ),
        migrations.AddField(
            model_name='ordercost',
            name='yearly_binding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendor',
            name='monthly_order',
            field=models.PositiveIntegerField(default=500),
        ),
    ]
