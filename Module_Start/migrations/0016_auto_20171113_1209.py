# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module_Start', '0015_auto_20171113_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='us_img1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='us_img2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
