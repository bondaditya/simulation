# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0012_auto_20170502_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand',
            name='demand_value',
        ),
    ]
