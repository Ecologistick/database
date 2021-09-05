import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                line[4] = datetime.strptime(line[4], "%Y-%m-%d")
                line[0] = int(line[0])
                phone = Phone(*line[0:-1], slug=line[1].replace(' ', '_'))
                phone.save()
                pass
