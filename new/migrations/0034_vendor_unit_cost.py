# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0033_remove_vendor_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='unit_cost',
            field=models.IntegerField(default=500, verbose_name='Cost per unit'),
        ),
    ]
