import django_filters
from .models import Movement

YEARS = (
    # (2000, 2000),
    # (2001, 2001),
    # (2002, 2002),
    # (2003, 2003),
    # (2004, 2004),
    # (2005, 2005),
    # (2006, 2006),
    # (2006, 2006),
    # (2006, 2006),
    # (2007, 2007),
    # (2008, 2008),
    # (2009, 2009),
    (2010, 2010),
    (2011, 2011),
    (2012, 2012),
    (2013, 2013),
    (2014, 2014),
    (2015, 2015),
    (2016, 2016),
    (2017, 2017),
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
)
MONTHS = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)

class MovementFilter(django_filters.FilterSet):
    '''Filter movements by year and by month'''
    date__year = django_filters.ChoiceFilter(choices=YEARS, label="Year: ")
    date__month = django_filters.ChoiceFilter(choices=MONTHS, label="Month: ")

    class Meta:
        model = Movement
        fields = {
            'date': ['year', 'month'],
        }

