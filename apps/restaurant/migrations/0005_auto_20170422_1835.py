# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20170422_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at'], 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
