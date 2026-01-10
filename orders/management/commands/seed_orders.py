from django.core.management.base import BaseCommand

from orders.models import Order


class Command(BaseCommand):
    help = "Seeds the database with example orders"

    def handle(self, *args, **kwargs):
        # Clear existing orders
        Order.objects.all().delete()

        # Create 3 example orders
        orders = [
            Order(total=100.50, items_count=1),
            Order(total=201.00, items_count=2),
            Order(total=301.50, items_count=3),
        ]

        Order.objects.bulk_create(orders)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {len(orders)} orders")
        )
