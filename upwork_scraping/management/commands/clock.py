from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from .scrape import BaseCommand as ScrapeCommand
from .send import BaseCommand as SendCommand

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=15)
def scrape():
    ScrapeCommand().handle()
    SendCommand().send()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler.start()
