from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {"pk": 1, "name": "Электроинструмент", "description": "Электроинструменты аккумуляторные и сетевые"},
            {"pk": 2, "name": "Ручной инструмент", "description": "Ручные инструменты различные"},
            {"pk": 3, "name": "Садовый инструмент", "description": "Садовые инструменты различные"},
            {"pk": 4, "name": "Бензоинструмент", "description": "Бензоинструмент различный"},
        ]

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)
        print('category ok')

        product_list = [
            {"name": "Молоток",
             "description": "Молоток ручной.",
             "category_id": 2,
             "price": 590,
             },
            {"name": "Шуруповерт",
             "description": "Шуруповерт аккумуляторный",
             "category_id": 1,
             "price": 3500,
             },
            {"name": "Лопата садовая",
             "description": "Лопата садовая металлическая с деревянной ручкой",
             "category_id": 3,
             "price": 1200,
             },
        ]

        product_for_create = []
        for product in product_list:
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)
        print('product ok')
