from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):
            Listing.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(),
                price_per_night=random.randint(50, 500),
                location=fake.city()
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
