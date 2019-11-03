from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from json import loads, dumps
from .filters import MovementFilter
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .models import Movement, Category, Type

#-------------------------------------------------------------------------------

class MovementListView(ListView):
    '''List of all the movements that the user has made.'''
    #model = Movement
    template_name = "finance/MainPage.html"
    context_object_name = 'Movements'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        #Overwritting the Listview to insert filter and add extra context
        context = super().get_context_data(**kwargs) 
        context['filter'] = MovementFilter(self.request.GET, self.get_queryset()) 
        # ^ filter used to limit by year and month
        context['serialized'] = serialize(
            'json', context['filter'].qs,
            fields=('Amount', 'category')
            )

        data = loads(context['serialized'])
        for d in data: #overwriting my json to change pk to name of each category
            d['fields']['category'] = Category.objects.get(pk=d['fields']['category']).name
        context['test'] = dumps(data)
        return context

    def get_queryset(self):
        '''Specifies that i only want the user that is currently logged in data.'''
        if self.request.user.is_authenticated:        
            return Movement.objects.filter(user=self.request.user)

#-------------------------------------------------------------------------------

class DateInput(forms.DateInput):
    '''Defines the date input i want.'''
    input_type = 'date'

#-------------------------------------------------------------------------------

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    '''The view that creates each Expense.'''
    model = Movement
    fields = ['description', 'Amount', 'category', 'date']
    template_name = "finance/Expense_form.html"

    def get_form(self, form_class=None):
        form = super(ExpenseCreateView, self).get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(type__name='Expense')
        form.fields['date'] = forms.DateField(widget=DateInput)
        return form

    def form_valid(self, form):
        form.instance.Amount = abs(form.cleaned_data['Amount']) * -1
        form.instance.type = Type.objects.get(name='Expense')
        form.instance.user = self.request.user
        return super().form_valid(form)

#-------------------------------------------------------------------------------

class IncomeCreateView(LoginRequiredMixin, CreateView):
    '''The view that creates each Income.'''
    model = Movement
    fields = ['description', 'Amount', 'category', 'date']
    template_name = "finance/Income_form.html"

    def get_form(self, form_class=None):
        form = super(IncomeCreateView, self).get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(type__name='Income')
        form.fields['date'] = forms.DateField(widget=DateInput)
        return form

    def form_valid(self, form):
        form.instance.Amount = abs(form.cleaned_data['Amount'])
        form.instance.type = Type.objects.get(name='Income')
        form.instance.user = self.request.user
        return super().form_valid(form)
