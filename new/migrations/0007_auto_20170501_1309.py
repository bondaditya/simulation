# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0006_auto_20170501_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='tax_total',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='total',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_cost',
        ),
        migrations.RemoveField(
            model_name='vendortotal',
            name='line_item_total',
        ),
        migrations.RemoveField(
            model_name='vendortotal',
            name='quantity',
        ),
    ]
