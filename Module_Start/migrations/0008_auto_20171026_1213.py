# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module_Start', '0007_page_us_jpg1'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='us_jpg2',
            field=models.ImageField(default='us_jpg2.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='us_jpg1',
            field=models.ImageField(default='us_jpg1.png', upload_to=''),
        ),
    ]
