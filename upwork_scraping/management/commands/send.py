from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from upwork_scraping import models
from django.utils import timezone
from pprint import pprint
import telepot


class Command(BaseCommand):
    def handle(self, *args, **options):
        yesterday = timezone.now().date() - timezone.timedelta(1)
        jobs = models.Job.objects.filter(date_created__gte=yesterday)
        bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
        response = bot.getUpdates()
        # for message in response:
        #     chat, is_new = models.Chat.objects.get_or_create(
        #         **message['message']['chat'])
        #     if is_new:
        #         chat.save()
        # for chat in models.Chat.objects.all():
        #     try:
        #         bot.sendMessage(chat.id, "\n\n".join(
        #             job.get_message() for job in jobs))
        #     except (telepot.exception.BotWasBlockedError, telepot.exception.BotWasKickedError):
        #         chat.delete()
        for job in jobs:
            bot.sendMessage(settings.TELEGRAM_CHANNEL_ID, job.get_message())
        pprint(response)
