# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Movement

# def home(request):
#    context = {
#       'title': 'Main Page',
#       'Movements' : Movement.objects.all()
#    }
#    return render(request, 'finance/MainPage.html',context)

class MovementListView(ListView): # pylint: disable=too-many-ancestors
    '''List of all the movements that the user has made.'''
    #model = Movement
    template_name = "finance/MainPage.html"
    context_object_name = 'Movements'
    ordering = ['-date']

    def get_queryset(self):
        '''Specifies that i only want the user that is currently logged in data.'''
        return Movement.objects.filter(user=self.request.user)

# class MovementDetailView(DetailView):
#    model = Movement

class DateInput(forms.DateInput):
    '''Defines the date input i want.'''
    input_type = 'date'

# pylint: disable=too-many-ancestors
class MovementCreateView(LoginRequiredMixin, CreateView):
    '''The view that creates each movement.'''
    model = Movement
    fields = ['description', 'Amount', 'date']

    def get_form(self, form_class=None):
        form = super(MovementCreateView, self).get_form(form_class)
        form.fields['date'] = forms.DateField(widget=DateInput)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
