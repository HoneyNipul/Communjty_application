# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-18 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0030_auto_20170415_1240'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='event_registery',
            new_name='eventInvitee',
        ),
        migrations.RenameModel(
            old_name='events',
            new_name='eventRegistration',
        ),
        migrations.AlterModelTable(
            name='eventinvitee',
            table='eventInvitee',
        ),
        migrations.AlterModelTable(
            name='eventregistration',
            table='eventRegistration',
        ),
    ]
