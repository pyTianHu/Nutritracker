import datetime
from django.utils import timezone
from Nutritracker_App.models import BodyWeight

def add_data():
    # Generate sample data (replace this with your actual data)
    data = [
        {'date': datetime.date(2021, 1, 1), 'bodyWeight': 150},
        {'date': datetime.date(2021, 1, 2), 'bodyWeight': 149},
        # Add more data as needed
    ]

    # Bulk create the objects
    BodyWeight.objects.bulk_create([
        BodyWeight(date=d['date'], bodyWeight=d['bodyWeight']) for d in data
    ])