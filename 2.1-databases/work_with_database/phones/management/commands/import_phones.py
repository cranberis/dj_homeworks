import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv", "r", encoding="utf-8") as file:
            phones = list(csv.DictReader(file, delimiter=";"))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone.pop("id", None)
            phone["lte_exists"] = phone["lte_exists"].lower() == "true"
            item = Phone(**phone)
            item.save()

        self.stdout.write(
            self.style.SUCCESS(f"Успешно импортировано {len(phones)} телефонов")
        )
