import json
from techex.models import Entry
from django.core.management.base import BaseCommand

# import daily file into database

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        f = open('transactions.json')

        data = json.load(f)

        # Iterating through the json
        # list
        for row in data:
            del row['$id']
            e = Entry(**row)
            e.save()
        # Closing file
        f.close()

