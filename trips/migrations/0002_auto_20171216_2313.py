# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='duration',
            new_name='duration_weeks',
        ),
    ]
