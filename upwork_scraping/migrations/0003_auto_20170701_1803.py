# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_scraping', '0002_auto_20170630_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('type', models.CharField(max_length=10, choices=[(b'private', b'Private'), (b'group', b'Group'), (b'channel', b'Channel')])),
                ('username', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
        migrations.AlterField(
            model_name='query',
            name='days_posted',
            field=models.IntegerField(default=1, help_text=b'Number of days since the job was posted', null=True),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
