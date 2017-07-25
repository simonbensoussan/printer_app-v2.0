# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 13:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import landing.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 7, 25, 13, 56, 42, 211817, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocks',
            name='updated_at',
            field=models.DateTimeField(default=landing.models.default_time),
        ),
    ]