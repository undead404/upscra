# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_scraping', '0003_auto_20170701_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='all_members_are_administrators',
            field=models.BooleanField(default=False),
        ),
    ]
