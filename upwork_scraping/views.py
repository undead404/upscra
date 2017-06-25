from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
import settings


def callback(request):
    pprint(dir(request))
    return HttpResponse(request.get_full_path())


def login_page(request):
    """import upwork
    client = upwork.Client(settings.UPWORK_OAUTH_KEY, settings.UPWORK_OAUTH_SECRET)
    print "Please to this URL (authorize the app if necessary):"
    print client.auth.get_authorize_url()"""
    return render(request, template_name='login_page.html')
