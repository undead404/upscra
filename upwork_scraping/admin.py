from django.contrib import admin

from .models import Chat, Job, Query

admin.site.register(Chat)
admin.site.register(Job)
admin.site.register(Query)
