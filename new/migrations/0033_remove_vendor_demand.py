# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0032_auto_20170504_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='demand',
        ),
    ]
