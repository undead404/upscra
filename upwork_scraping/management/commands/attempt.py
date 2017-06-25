from django.core.management.base import BaseCommand, CommandError
# from fake_useragent import UserAgent
from upwork_scraping.models import Skill, Job
from pprint import pprint
# import requests
import upwork


public_key = 'b5a378f9f9db6c67ba19049a7f4adecb'
secret_key = 'a27906e32f044acc'
oauth_access_token = 'c8d9db0d88b385461cc7cdf81ade39f4'
oauth_access_token_secret = 'ec314b49b0396230'

class Command(BaseCommand):
    def handle(self, *args, **options):
        client = upwork.Client(public_key, secret_key)
        # print "Please to this URL (authorize the app if necessary):"
        # print client.auth.get_authorize_url()
        # print "After that you should be redirected back to your app URL with " + \
        #     "additional ?oauth_verifier= parameter"
        # verifier = raw_input('Enter oauth_verifier: ')

        # oauth_access_token, oauth_access_token_secret = \
        #     client.auth.get_access_token(verifier)
        # self.stdout.write(oauth_access_token +', ' + oauth_access_token_secret)

        # Instantiating a new client, now with a token.
        # Not strictly necessary here (could just set `client.oauth_access_token`
        # and `client.oauth_access_token_secret`), but typical for web apps,
        # which wouldn't probably keep client instances between requests
        client = upwork.Client(public_key, secret_key,
                              oauth_access_token=oauth_access_token,
                              oauth_access_token_secret=oauth_access_token_secret)
        skill, is_new = Skill.objects.get_or_create(name="python")
        if is_new:
            skill.save()
        # data = {'skills': 'python'}
        for skill in Skill.objects.all():
            response = client.provider_v2.search_jobs(data={"skills": skill.name})
            for job_dict in response:
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
                print job_data['title'] + '(' + ', '.join(job_dict['skills']) + ')'
                job_data['url'] = job_dict['url']
                if job_dict['workload'] is None:
                    job_data['workload'] = ''
                else:
                    job_data['workload'] = job_dict['workload']
                job = Job(**job_data)
                job.save()

                for skill_name in job_dict['skills']:
                    skill, is_new = Skill.objects.get_or_create(name=skill_name)
                    if is_new:
                        skill.save()
                    job.skills.add(skill)