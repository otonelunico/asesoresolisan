# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module_Start', '0004_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='us',
            field=models.TextField(default='Sin Texto'),
        ),
        migrations.AlterField(
            model_name='page',
            name='note',
            field=models.TextField(default='Sin Texto'),
        ),
    ]
