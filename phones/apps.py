# apps.py

from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import your_app_name.import_phones  # Импортируйте ваш скрипт для переноса данных
