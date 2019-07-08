# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-26 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_visitview_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=128, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='分类名称'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='web',
            name='name',
            field=models.CharField(max_length=64, verbose_name='网站名字'),
        ),
        migrations.AlterField(
            model_name='webcategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name='网站类别'),
        ),
    ]