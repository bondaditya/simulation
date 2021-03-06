# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cost_index', models.DecimalField(decimal_places=1, max_digits=50)),
                ('delivery_index', models.DecimalField(decimal_places=1, max_digits=50)),
                ('quality_index', models.DecimalField(decimal_places=1, max_digits=50)),
                ('yearly_binding', models.BooleanField(default=False)),
                ('delivery_time', models.IntegerField(default=30)),
                ('rm_cost', models.IntegerField(default=500)),
            ],
        ),
        migrations.AddField(
            model_name='marketing',
            name='total_marketing',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
