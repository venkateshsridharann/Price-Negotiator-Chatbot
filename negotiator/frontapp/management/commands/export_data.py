import csv
from django.core.management.base import BaseCommand
from frontapp.models import Product

class Command(BaseCommand):
    help = 'Export data to CSV'

    def handle(self, *args, **kwargs):
        # Define the file path and name
        file_path = 'export2.csv'
        
        # Fetch the data from your model
        data = Product.objects.all()

        # Define the CSV column headers
        headers = [field.name for field in Product._meta.fields]

        # Write to the CSV file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)  # Write headers
            for obj in data:
                writer.writerow([getattr(obj, field) for field in headers])  # Write data

        self.stdout.write(self.style.SUCCESS(f'Data exported to {file_path}'))