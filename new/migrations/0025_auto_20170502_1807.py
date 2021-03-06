# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0024_auto_20170502_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demand',
            old_name='monthly_demand_discount_2',
            new_name='monthly_demand_discount_average',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_discount_3',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_discount_4',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_marketing_1',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_marketing_2',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_marketing_3',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='monthly_demand_marketing_4',
        ),
        migrations.AddField(
            model_name='demand',
            name='monthly_demand_flavour_average',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='demand',
            name='monthly_demand_marketing_average',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=5),
        ),
    ]
