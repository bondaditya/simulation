# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20170429_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costs',
            name='rm_cost_unit',
        ),
        migrations.AddField(
            model_name='costs',
            name='rm_cost_total',
            field=models.DecimalField(decimal_places=2, default=250.0, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_cost',
            field=models.DecimalField(decimal_places=2, default=250, max_digits=50),
            preserve_default=False,
        ),
    ]