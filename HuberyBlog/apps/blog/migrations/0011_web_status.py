# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-26 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190626_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '无效'), (1, '有效')], default=1, verbose_name='是否有效'),
        ),
    ]