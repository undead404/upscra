# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='query',
            field=models.ForeignKey(related_name='jobs', on_delete=django.db.models.deletion.SET_NULL, to='upwork_scraping.Query', null=True),
        ),
    ]
