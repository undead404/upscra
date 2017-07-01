# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('budget', models.IntegerField(default=0)),
                ('category2', models.CharField(max_length=50)),
                ('client_country', models.CharField(max_length=200, blank=True)),
                ('client_feedback', models.FloatField(default=0.0)),
                ('client_jobs_posted', models.IntegerField(default=0)),
                ('client_past_hires', models.IntegerField(default=0)),
                ('client_payment_verification_status', models.CharField(max_length=50, blank=True)),
                ('client_reviews_count', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField()),
                ('id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('job_status', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=50)),
                ('snippet', models.TextField()),
                ('subcategory2', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(editable=False)),
                ('workload', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('budget', models.CharField(help_text=b'A number or range used to filter the search by jobs having a budget equal to, more or less than, or within the values provided. For example: `[100 TO 1000]` - the budget is between 100 and 1000; `1000` - the budget is equal to 1000. `500-1000` - the budget `b` is 500 <= b <= 1000, `1000-` - the budget is >=1000; `-200` - the budget is <= 200', max_length=50, blank=True)),
                ('category2', models.CharField(help_text=b"The category (V2) of the freelancer's profile. Use Metadata resource to get it. You can get it via Metadata Category (v2) resource", max_length=50, blank=True)),
                ('client_feedback', models.CharField(help_text=b'A number or range used to filter the search by jobs posted by clients with a rating equal to, more or less than, or within the values provided. If the value is `None`, then jobs from clients without rating are returned. Single parameters such as `1` or `2,3` are valid (comma separated values result in `OR` queries). Ranges such as `[2 TO 4]` are also valid. Examples: `5.0` - the rating is equal to 5.0; `1-5` - the rating is so that 1 <= n <= 5; `1-` - the rating is >=1; `-5` - the rating is <= 5', max_length=50, blank=True)),
                ('client_hires', models.CharField(help_text=b'A number or range used to filter the search by clients with a number of past hires equal to, more or less than, or within the values provided. Single parameters such as `1` or `2,3` are valid (comma-separated values result in `OR` queries). Ranges such as `[10 TO 20]` are also valid. Examples: `5` - the number of past hires is to 5; `0-10`: number of past hires is 0 <= n <= 10; `10-` - the number of past hires is >=10; `-5` - the number of past hires is <= 5', max_length=50, blank=True)),
                ('days_posted', models.IntegerField(help_text=b'Number of days since the job was posted', null=True, blank=True)),
                ('duration', models.CharField(default=b'', help_text=b'The duration of the job', max_length=20, blank=True, choices=[(b'', b'Any'), (b'week', b'Week'), (b'month', b'Month'), (b'quarter', b'Quarter'), (b'semester', b'Semester'), (b'ongoing', b'Ongoing')])),
                ('job_status', models.CharField(default=b'', help_text=b'The current status of the Job', max_length=20, blank=True, choices=[(b'', b'Any'), (b'open', b'Open'), (b'completed', b'Completed'), (b'cancelled', b'Cancelled')])),
                ('job_type', models.CharField(default=b'', help_text=b'The type of the Job', max_length=20, blank=True, choices=[(b'', b'Any'), (b'hourly', b'Hourly'), (b'fixed-price', b'Fixed price')])),
                ('q', models.CharField(help_text=b'The search query', max_length=200, blank=True)),
                ('skills', models.CharField(help_text=b"Searches for skills in the job's profile", max_length=200, blank=True)),
                ('subcategory2', models.CharField(help_text=b'The subcategory of the job according to the list of Categories 2.0. Example: `Web & Mobile Development`. You can get it via Metadata Category (v2) resource', max_length=50, blank=True)),
                ('title', models.CharField(help_text=b"Searches for the title of the job's profile", max_length=200, blank=True)),
                ('workload', models.CharField(default=b'', help_text=b'Indicates the workload for the job', max_length=20, blank=True, choices=[(b'', b'Any'), (b'as_needed', b'As needed'), (b'part_time', b'Part-time'), (b'full_time', b'Full-time')])),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='job',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='upwork_scraping.Query', null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(related_name='jobs', to='upwork_scraping.Skill'),
        ),
    ]
