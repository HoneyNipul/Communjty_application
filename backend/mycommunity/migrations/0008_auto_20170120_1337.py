# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0007_auto_20170120_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(max_length=16),
        ),
    ]
