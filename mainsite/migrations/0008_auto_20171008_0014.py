# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20171007_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastime',
            name='view',
        ),
        migrations.AlterField(
            model_name='pastime',
            name='category',
            field=models.CharField(choices=[('M', 'Movie'), ('B', 'Book'), ('G', 'Game'), ('A', 'Animation'), ('O', 'Other')], max_length=1, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='pastime',
            name='finTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pastime',
            name='illustration',
            field=models.CharField(max_length=255, verbose_name='配图'),
        ),
        migrations.AlterField(
            model_name='pastime',
            name='name',
            field=models.CharField(max_length=31, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='illustration',
            field=models.CharField(max_length=255, verbose_name='配图'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=127, unique=True, verbose_name='链接名'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='mainsite.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=127, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=63, verbose_name='标签名'),
        ),
    ]
