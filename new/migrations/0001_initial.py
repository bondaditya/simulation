# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True)),
                ('embed_code', models.TextField()),
                ('free', models.BooleanField(default=True)),
                ('member_required', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
