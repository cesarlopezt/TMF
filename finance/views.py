from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Movement

CATEGORIES = (
    ('Ed', 'Education'),
    ('Tr', 'Trasportation'),
    ('Ho', 'Home'),
    ('Gr', 'Groceries'),
    ('PC', 'Personal Care'),
    ('Tv', 'Travel'),
    ('Gv', 'Giving'),
    ('In', 'Investment'),
    ('Fo', 'Food'),
    ('En', 'Entertainment'),
    ('Gs', 'Gas'),
    ('Sb', 'Subscriptions'),
    ('UN', 'Uncategorized')
)

class MovementListView(ListView): # pylint: disable=too-many-ancestors
    '''List of all the movements that the user has made.'''
    #model = Movement
    template_name = "finance/MainPage.html"
    context_object_name = 'Movements'
    ordering = ['-date']

    def get_queryset(self):
        '''Specifies that i only want the user that is currently logged in data.'''
        return Movement.objects.filter(user=self.request.user)

class DateInput(forms.DateInput):
    '''Defines the date input i want.'''
    input_type = 'date'

# pylint: disable=too-many-ancestors
class MovementCreateView(LoginRequiredMixin, CreateView):
    '''The view that creates each movement.'''
    model = Movement
    fields = ['description', 'Amount','category', 'date']

    def get_form(self, form_class=None):
        form = super(MovementCreateView, self).get_form(form_class)
        form.fields['category'] = forms.ChoiceField(choices=CATEGORIES)
        form.fields['date'] = forms.DateField(widget=DateInput)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
