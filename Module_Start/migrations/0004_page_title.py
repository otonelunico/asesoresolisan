# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module_Start', '0003_auto_20171024_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.TextField(default='Sin Texto'),
        ),
    ]
