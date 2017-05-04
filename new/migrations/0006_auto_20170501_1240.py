# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0005_auto_20170501_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_requirement', models.PositiveIntegerField(default=500)),
                ('monthly_order', models.PositiveIntegerField(default=500)),
                ('order_fraction', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('monthly_cost', models.PositiveIntegerField(default=0)),
                ('yearly_cost', models.PositiveIntegerField(default=0)),
                ('total_cost', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('no_of_months', models.PositiveIntegerField(default=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='rm_cost',
        ),
        migrations.AddField(
            model_name='vendor',
            name='unit_cost',
            field=models.IntegerField(default=500, verbose_name='Cost per unit'),
        ),
    ]
