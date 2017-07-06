from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from upwork_scraping import models
from django.utils import timezone
import telepot


class Command(BaseCommand):
    def handle(self, *args, **options):
        yesterday = timezone.now().date() - timezone.timedelta(1)
        jobs = models.Job.objects.filter(
            date_created__gte=yesterday, is_shown=False)
        bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
        response = bot.getUpdates()
        for job in jobs:
            bot.sendMessage(job.query.channel_id, job.get_message())
            job.is_shown = True
            job.save()
