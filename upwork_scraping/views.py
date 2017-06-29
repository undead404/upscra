from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
# from django_upwork_auth import utils as upwork_auth_utils
# from django_upwork_auth import settings as upwork_auth_settings
from pprint import pprint
from .models import Query
import upwork


"""def callback(request):
    uri = request.get_full_path().split('?')[-1]
    i1 = uri.index('oauth_token=') + len('oauth_token')
    i2 = uri.find('&', i1)
    oauth_token = uri[i1:i2]
    i1 = uri.index('oauth_verifier=') + len('oauth_verifier=')
    i2 = uri.find('&', i1)
    oauth_verifier = uri[i1:i2]
    client = upwork.Client(settings.UPWORK_OAUTH_KEY, settings.UPWORK_OAUTH_SECRET)
    oauth_access_token, oauth_access_token_secret = client.auth.get_access_token(
        oauth_verifier)

    # Instantiating a new client, now with a token.
    # Not strictly necessary here (could just set `client.oauth_access_token`
    # and `client.oauth_access_token_secret`), but typical for web apps,
    # which wouldn't probably keep client instances between requests
    client = upwork.Client(public_key, secret_key, oauth_access_token=oauth_access_token,
                           oauth_access_token_secret=oauth_access_token_secret)
    pprint(dict(request.session))
    client = upwork_auth_utils.get_client(
        request.session[upwork_auth_settings.ACCESS_TOKEN_SESSION_KEY])
    # access = [request.GET['oauth_token'], request.GET['oauth_verifier']]
    access = request.session[upwork_auth_settings.ACCESS_TOKEN_SESSION_KEY]
    pprint(access)
    pprint(upwork_auth_utils.check_login(access))
    # import ipdb
    # ipdb.set_trace()
    # client = upwork_auth_utils.get_client([request.GET['oauth_token'], request.GET['oauth_verifier'])
    jobs_num = 0
    for query in Query.objects.all():
        # print(query)
        response = client.provider_v2.search_jobs(data=query.get_key_values())
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
        jobs_num += len(response)
    return HttpResponse("{} jobs scraped.".format(jobs_num))"""


def login_page(request):
    """import upwork
    client = upwork.Client(settings.UPWORK_OAUTH_KEY, settings.UPWORK_OAUTH_SECRET)
    print "Please to this URL (authorize the app if necessary):"
    print client.auth.get_authorize_url()"""
    return render(request, template_name='login_page.html')
