# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0008_auto_20170501_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.PositiveIntegerField(default=12000)),
                ('monthly_demand', models.PositiveIntegerField(default=1000)),
                ('new_style', models.BooleanField(default=False)),
                ('new_flavour', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('marketing', models.BooleanField(default=False)),
            ],
        ),
    ]
