from cached_property import cached_property
from django.core.exceptions import ValidationError
from django.db import models


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
    is_shown = models.BooleanField(default=False)
    job_status = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    query = models.ForeignKey(
        "Query", null=True, on_delete=models.SET_NULL, related_name="jobs")
    snippet = models.TextField()
    subcategory2 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField(editable=False)
    workload = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_message(self):
        return "[{budget}$] {title} {url}".format(budget=self.budget, title=self.title, url=self.url)

    @staticmethod
    def from_dict(job_dict):
        job_data = {}
        job_data['budget'] = job_dict['budget']
        job_data['category2'] = job_dict['category2']
        if job_dict['client']['country'] is None:
            job_data['client_country'] = ''
        else:
            job_data['client_country'] = job_dict['client']['country']
        job_data['client_feedback'] = job_dict['client']['feedback']
        job_data['client_jobs_posted'] = job_dict['client']['jobs_posted']
        job_data['client_past_hires'] = job_dict['client']['past_hires']
        if job_dict['client']['payment_verification_status'] is None:
            job_data['client_payment_verification_status'] = ''
        else:
            job_data['client_payment_verification_status'] = job_dict['client']['payment_verification_status']
        job_data['client_reviews_count'] = job_dict['client']['reviews_count']
        job_data['date_created'] = job_dict['date_created']
        # job_data['duration'] = job_dict['duration']
        job_data['id'] = job_dict['id']
        job_data['job_status'] = job_dict['job_status']
        job_data['job_type'] = job_dict['job_type']
        job_data['snippet'] = job_dict['snippet']
        job_data['subcategory2'] = job_dict['subcategory2']
        job_data['title'] = job_dict['title']
        job_data['url'] = job_dict['url']
        if job_dict['workload'] is None:
            job_data['workload'] = ''
        else:
            job_data['workload'] = job_dict['workload']
        job, is_new = Job.objects.update_or_create(
            id=job_data['id'], defaults=job_data)
        if is_new:
            print job_data['title'] + '(' + ', '.join(job_dict['skills']) + ')'
        return job, is_new

    class Meta:
        get_latest_by = 'date_created'
        ordering = ['-date_created']


class Query(models.Model):
    budget = models.CharField(
        blank=True, help_text="A number or range used to filter the search by jobs having a budget equal to, more or less than, or within the values provided. For example: `[100 TO 1000]` - the budget is between 100 and 1000; `1000` - the budget is equal to 1000. `500-1000` - the budget `b` is 500 <= b <= 1000, `1000-` - the budget is >=1000; `-200` - the budget is <= 200", max_length=50)
    category2 = models.CharField(
        blank=True, help_text="The category (V2) of the freelancer's profile. Use Metadata resource to get it. You can get it via Metadata Category (v2) resource", max_length=50)
    channel_id = models.IntegerField()
    client_feedback = models.CharField(
        blank=True, help_text="A number or range used to filter the search by jobs posted by clients with a rating equal to, more or less than, or within the values provided. If the value is `None`, then jobs from clients without rating are returned. Single parameters such as `1` or `2,3` are valid (comma separated values result in `OR` queries). Ranges such as `[2 TO 4]` are also valid. Examples: `5.0` - the rating is equal to 5.0; `1-5` - the rating is so that 1 <= n <= 5; `1-` - the rating is >=1; `-5` - the rating is <= 5", max_length=50)
    client_hires = models.CharField(
        blank=True, help_text="A number or range used to filter the search by clients with a number of past hires equal to, more or less than, or within the values provided. Single parameters such as `1` or `2,3` are valid (comma-separated values result in `OR` queries). Ranges such as `[10 TO 20]` are also valid. Examples: `5` - the number of past hires is to 5; `0-10`: number of past hires is 0 <= n <= 10; `10-` - the number of past hires is >=10; `-5` - the number of past hires is <= 5", max_length=50)
    days_posted = models.IntegerField(
        default=1, help_text="Number of days since the job was posted", null=True)
    DURATIONS = (('', 'Any'), ('week', 'Week'), ('month', 'Month'),
                 ('quarter', 'Quarter'), ('semester', 'Semester'), ('ongoing', 'Ongoing'))
    duration = models.CharField(blank=True, choices=DURATIONS,
                                default='', help_text="The duration of the job", max_length=20)
    JOB_STATUSES = (('', 'Any'), ('open', 'Open'),
                    ('completed', 'Completed'), ('cancelled', 'Cancelled'))
    job_status = models.CharField(blank=True, choices=JOB_STATUSES,
                                  default='open', help_text="The current status of the Job", max_length=20)
    JOB_TYPES = (('', 'Any'), ('hourly', 'Hourly'),
                 ('fixed-price', 'Fixed price'))
    job_type = models.CharField(blank=True, choices=JOB_TYPES,
                                default='', help_text="The type of the Job", max_length=20)
    __key_values = None
    q = models.CharField(
        blank=True, help_text="The search query", max_length=200)
    skills = models.CharField(
        blank=True, help_text="Searches for skills in the job's profile", max_length=200)
    subcategory2 = models.CharField(
        blank=True, help_text="The subcategory of the job according to the list of Categories 2.0. Example: `Web & Mobile Development`. You can get it via Metadata Category (v2) resource", max_length=50)
    title = models.CharField(
        blank=True, help_text="Searches for the title of the job's profile", max_length=200)
    WORKLOADS = (('', 'Any'), ('as_needed', 'As needed'),
                 ('part_time', 'Part-time'), ('full_time', 'Full-time'))
    workload = models.CharField(blank=True, choices=WORKLOADS, default='',
                                help_text="Indicates the workload for the job", max_length=20)

    def __str__(self):
        # key_values = self.get_key_values()
        return '&'.join('{key}={value}'.format(key=key, value=key_values[key]) for key in self.key_values())

    def clean(self):
        if not (self.q or self.skills or self.title):
            raise ValidationError(
                "You must specify either q or skills or title")

    # def get_key_values(self):
    #     if self.__key_values:
    #         return self.__key_values
    #     self.__key_values = {}
    #     if self.budget:
    #         self.__key_values['budget'] = self.budget
    #     if self.category2:
    #         self.__key_values['category2'] = self.category2
    #     if self.client_feedback:
    #         self.__key_values['client_feedback'] = self.client_feedback
    #     if self.client_hires:
    #         self.__key_values['client_hires'] = self.client_hires
    #     if self.days_posted is not None:
    #         self.__key_values['days_posted'] = self.days_posted
    #     if self.duration:
    #         self.__key_values['duration'] = self.duration
    #     if self.job_status:
    #         self.__key_values['job_status'] = self.job_status
    #     if self.job_type:
    #         self.__key_values['job_type'] = self.job_type
    #     if self.q:
    #         self.__key_values['q'] = self.q
    #     if self.skills:
    #         self.__key_values['skills'] = self.skills
    #     if self.subcategory2:
    #         self.__key_values['subcategory2'] = self.subcategory2
    #     if self.title:
    #         self.__key_values['title'] = self.title
    #     if self.workload:
    #         self.__key_values['workload'] = self.workload
    #     return self.__key_values
    @cached_property
    def key_values(self):
        keys = ['budget', 'category2', 'client_feedback', 'client_hires', 'duration', 'job_status',
                'job_type', 'q', 'skills', 'subcategory2', 'title', 'workload']
        key_values = {k: getattr(self, k) for k in keys if getattr(self, k)}
        if self.days_posted is not None:
            self.key_values['days_posted'] = self.days_posted
        return key_values
