# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0013_remove_demand_demand_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='demand_value',
            field=models.PositiveIntegerField(default=120000),
        ),
    ]
