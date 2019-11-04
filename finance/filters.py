import django_filters
from .models import Movement

class MovementFilter(django_filters.FilterSet):
    '''Filter movements by year and by month'''
    class Meta:
        model = Movement
        fields = {
            'date': ['year', 'month'],
        }
