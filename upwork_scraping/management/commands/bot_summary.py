from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pprint import pprint
import telepot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
        response = bot.getUpdates()
        pprint(response)
