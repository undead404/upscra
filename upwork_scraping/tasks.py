from celery import shared_task
from management.commands.scrape import Command as ScrapeCommand
from management.commands.send import Command as SendCommand


@shared_task()
def scrape_and_send():
    ScrapeCommand().handle()
    SendCommand().handle()
