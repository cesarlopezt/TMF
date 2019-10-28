import django_filters 
from .models import Movement

class MovementFilter(django_filters.FilterSet):
    class Meta:
        model = Movement
        fields = {
            'date': ['year', 'month'],
        }
