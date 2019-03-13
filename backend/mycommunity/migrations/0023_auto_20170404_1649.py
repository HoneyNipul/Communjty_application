# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-04 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0022_auto_20170404_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_registery',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
        migrations.AlterField(
            model_name='eventnotification',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
        migrations.AlterField(
            model_name='eventnotification',
            name='notification_type',
            field=models.CharField(max_length=1056),
        ),
        migrations.AlterField(
            model_name='invitelist',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
    ]
