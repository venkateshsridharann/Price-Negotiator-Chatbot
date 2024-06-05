import csv
from django.core.management.base import BaseCommand
from frontapp.models import Product

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            print(reader)
            for row in reader:
                print(row)
                product = Product(
                    title=row['ï»¿Title'],
                    listed_price=float(row['Listed Price']),
                    min_profitable_price=float(row['Minimum Profitable Price']),
                    category=row['Category'],
                    image=row['Image'],
                    
                     
                )
                product.save()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


        
