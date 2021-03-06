# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0014_demand_demand_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='monthly_demand_discount',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='demand',
            name='monthly_demand_flavour',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='demand',
            name='monthly_demand_marketing',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=5),
        ),
    ]
