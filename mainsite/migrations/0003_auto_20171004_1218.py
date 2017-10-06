# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20170927_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default='请输入摘要', verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='illustration',
            field=models.CharField(max_length=256, null=True, verbose_name='配图'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=256, verbose_name='链接名'),
        ),
    ]