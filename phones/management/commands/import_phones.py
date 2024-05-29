import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from your_app.models import Phone  # Замените 'your_app' на имя вашего приложения

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('path/to/your/csvfile.csv', newline='', encoding='utf-8') as csvfile:  # Укажите путь к вашему CSV файлу
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                Phone.objects.create(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'].lower() == 'true',
                    slug=slugify(row['name'])
                )
