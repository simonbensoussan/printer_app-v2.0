# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20170713_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='your img path', max_length=10000, verbose_name='image du produit'),
        ),
    ]
