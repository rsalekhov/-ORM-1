# import_phones.py

import csv
from django.core.management.base import BaseCommand
from myapp.models import Phone  # Замените 'myapp' на имя вашего приложения

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('path/to/your/csvfile.csv', newline='') as csvfile:  # Укажите путь к вашему CSV файлу
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                Phone.objects.create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
