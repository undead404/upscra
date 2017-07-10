from django.core.management.base import BaseCommand, CommandError
# from fake_useragent import UserAgent
from upwork_scraping.models import Job, Query
from pprint import pprint
from django.conf import settings
# import requests
import upwork


public_key = settings.UPWORK_OAUTH_KEY
secret_key = settings.UPWORK_OAUTH_SECRET
JOBS_NUM_PER_PAGE = 100
# oauth_access_token = 'c8d9db0d88b385461cc7cdf81ade39f4'
# oauth_access_token_secret = 'ec314b49b0396230'


class Command(BaseCommand):
    def handle(self, *args, **options):
        """client = upwork.Client(public_key, secret_key)
        print "Please to this URL (authorize the app if necessary):"
        print client.auth.get_authorize_url()
        print "After that you should be redirected back to your app URL with " + \
            "additional ?oauth_verifier= parameter"
        verifier = raw_input('Enter oauth_verifier: ')

        oauth_access_token, oauth_access_token_secret = \
            client.auth.get_access_token(verifier)
        self.stdout.write(oauth_access_token +', ' + oauth_access_token_secret)"""

        # Instantiating a new client, now with a token.
        # Not strictly necessary here (could just set `client.oauth_access_token`
        # and `client.oauth_access_token_secret`), but typical for web apps,
        # which wouldn't probably keep client instances between requests
        client = upwork.Client(settings.UPWORK_OAUTH_KEY, settings.UPWORK_OAUTH_SECRET,
                               oauth_access_token=settings.UPWORK_OAUTH_ACCESS_TOKEN, oauth_access_token_secret=settings.UPWORK_OAUTH_ACCESS_TOKEN_SECRET)
        jobs_num = 0
        for query in Query.objects.all():
            print(query)
            offset = 0
            while True:
                data = query.key_values()
                # data['page'] = "{offset};{count}".format(
                #     count=JOBS_NUM_PER_PAGE, offset=offset)
                response = client.provider_v2.search_jobs(
                    data=data, page_offset=offset, page_size=JOBS_NUM_PER_PAGE)
                # pprint(response)
                for job_dict in response:
                    job, is_new = Job.from_dict(job_dict)
                    if is_new:
                        job.query = query
                        job.save()
                        jobs_num += 1
                if len(response) < JOBS_NUM_PER_PAGE:
                    print(len(response), JOBS_NUM_PER_PAGE)
                    break
                offset += JOBS_NUM_PER_PAGE
        print("{} jobs scraped.".format(jobs_num))
