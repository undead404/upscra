from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Job(models.Model):
    budget = models.IntegerField(default=0)
    category2 = models.CharField(max_length=50)
    client_country = models.CharField(blank=True, max_length=200)
    client_feedback = models.FloatField(default=0.0)
    client_jobs_posted = models.IntegerField(default=0)
    client_past_hires = models.IntegerField(default=0)
    client_payment_verification_status = models.CharField(
        max_length=50, blank=True)
    client_reviews_count = models.IntegerField(default=0)
    date_created = models.DateTimeField()
    # duration
    id = models.CharField(primary_key=True, max_length=50)
    job_status = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, related_name="jobs")
    snippet = models.TextField()
    subcategory2 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField()
    workload = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_created']


class Query(models.Model):
    budget = models.CharField(blank=True, max_length=50)
    category2 = models.CharField(blank=True, max_length=50)
    client_feedback = models.CharField(blank=True, max_length=50)
    client_hires = models.CharField(blank=True, max_length=50)
    days_posted = models.IntegerField(null=True)
    DURATIONS = (('', 'Any'), ('week', 'Week'), ('month', 'Month'),
                 ('quarter', 'Quarter'), ('semester', 'Semester'), ('ongoing', 'Ongoing'))
    duration = models.CharField(
        blank=True, choices=DURATIONS, default='', max_length=20)
    JOB_STATUSES = (('', 'Any'), ('open', 'Open'),
                    ('completed', 'Completed'), ('cancelled', 'Cancelled'))
    job_status = models.CharField(
        blank=True, choices=JOB_STATUSES, default='', max_length=20)
    JOB_TYPES = (('', 'Any'), ('hourly', 'Hourly'),
                    ('fixed-price', 'Fixed price'))
    job_type = models.CharField(
        blank=True, choices=JOB_TYPES, default='', max_length=20)
    q = models.CharField(blank=True, max_length=200)
    skills = models.CharField(blank=True, max_length=200)
    subcategory2 = models.CharField(blank=True, max_length=50)
    title = models.CharField(blank=True, max_length=200)
    WORKLOADS = (('', 'Any'), ('as_needed', 'As needed'),
                 ('part_time', 'Part-time'), ('full_time', 'Full-time'))
    workload = models.CharField(
        blank=True, choices=WORKLOADS, default='', max_length=20)

    def clean(self):
        if not (self.q or self.skills or self.title):
            raise ValidationError(
                "You must specify either q or skills or title")
