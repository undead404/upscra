# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_scraping', '0006_auto_20170706_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='channel_id',
            field=models.IntegerField(),
        ),
    ]
