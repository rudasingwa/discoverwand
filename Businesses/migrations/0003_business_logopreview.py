# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Businesses', '0002_auto_20160825_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='LogoPreview',
            field=models.FileField(default=True, upload_to=b''),
        ),
    ]
