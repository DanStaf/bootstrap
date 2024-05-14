from django.core.management import BaseCommand
from catalog.models import Category, Product
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_data = [
            {'name': 'Фрукты', 'description': 'Сладкие фрукты'},
            {'name': 'Овощи', 'description': 'Свежие овощи'},
            {'name': 'Техника', 'description': 'Электроника'},
            {'name': 'Игрушки', 'description': 'Детские'},
        ]

        Category.objects.bulk_create([Category(**item) for item in categories_data])

        #for item in categories_data:
        #    Category.objects.create(**item)

        """data_list = []

        for item in categories_data:
            data_list.append(Category(**item))

        Category.objects.bulk_create(data_list)"""

        date_of_creation = datetime.now()

        products_data = [
            {'name': 'Яблоки', 'description': 'Красные', 'order_price': 100, 'category': Category.objects.get(name='Фрукты'),
             'created_at': date_of_creation, 'updated_at': date_of_creation},
            {'name': 'Апельсины', 'description': 'Марокко', 'order_price': 150,
             'created_at': date_of_creation, 'updated_at': date_of_creation},
            {'name': 'Бананы', 'description': 'Африка', 'order_price': 120,
             'created_at': date_of_creation, 'updated_at': date_of_creation},
            {'name': 'Телевизор', 'description': '100 дюймов', 'order_price': 100000,
             'created_at': date_of_creation, 'updated_at': date_of_creation},
            {'name': 'Смартфон', 'description': 'Samsung', 'order_price': 20000,
             'created_at': date_of_creation, 'updated_at': date_of_creation},
            {'name': 'Помидоры', 'description': 'Красные', 'order_price': 300,
             'created_at': date_of_creation, 'updated_at': date_of_creation},
        ]

        Product.objects.bulk_create([Product(**item) for item in products_data])