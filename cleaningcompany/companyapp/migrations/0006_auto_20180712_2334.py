# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-12 23:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0005_auto_20180411_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_bot_level',
            name='MiddleMenu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='menu_bot_level',
        ),
    ]
