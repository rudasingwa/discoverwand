# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-25 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Businesses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='Business_Category',
            new_name='Bznss_Category',
        ),
    ]
