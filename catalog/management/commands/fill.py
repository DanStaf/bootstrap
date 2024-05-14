from django.core.management import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_data = [
            {'name': 'Овощи', 'description': 'Свежие овощи'},
            {'name': 'Техника', 'description': 'Электроника'},
            {'name': 'Игрушки', 'description': 'Детские'},
        ]

        #for item in categories_data:
        #    Category.objects.create(**item)

        data_list = []

        for item in categories_data:
            data_list.append(Category(**item))

        Category.objects.bulk_create(data_list)
