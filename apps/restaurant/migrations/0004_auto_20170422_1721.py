# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('author', 'restaurant')]),
        ),
    ]
