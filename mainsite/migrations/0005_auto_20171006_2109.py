# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-06 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20171004_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=256, unique=True, verbose_name='链接名'),
        ),
    ]
