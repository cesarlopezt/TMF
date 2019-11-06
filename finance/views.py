from json import loads, dumps
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.core.serializers import serialize
from .filters import MovementFilter
from .models import Movement, Category, Type

#-------------------------------------------------------------------------------

class MovementListView(ListView):
    '''List of all the movements that the user has made.'''
    template_name = "finance/MainPage.html"
    context_object_name = 'Movements'

    def get_queryset(self):
        '''Specifies that i only want the user that is currently logged in data.'''
        if self.request.user.is_authenticated:        
            return Movement.objects.filter(user=self.request.user).order_by('-date')
            #Sends the queryset ordered by date

    def get_context_data(self, **kwargs):
        #Overwritting the Listview to insert filter and add extra context
        context = super().get_context_data(**kwargs)
        context['filter'] = MovementFilter(self.request.GET, self.get_queryset())
        # ^ filter used to limit by year and month
        context['serialized'] = serialize(
            'json',
            context['filter'].qs,
            fields=('Amount', 'category', 'type')
            )

        data = loads(context['serialized'])
        for d in data: #overwriting my json to change pk to name of each category
            d['fields']['category'] = Category.objects.get(pk=d['fields']['category']).name
        context['serialized'] = dumps(data)

        labelsIncome = [] #Lists that i fill to send to the json
        dataIncome = []
        labelsExpense = []
        dataExpense = []
        sum_income = 0
        sum_expense = 0
      
        def Selector(d, listLabels, listData):
            #Just one function to use in income and expenses
            if d['fields']['category'] not in listLabels:
                #adds a new category and its amount
                listLabels.append(d['fields']['category'])
                listData.append(d['fields']['Amount'])
            else:
                #sum to a category new amount
                index = listLabels.index(d['fields']['category'])
                listData[index] = float(listData[index])
                listData[index] += float(d['fields']['Amount'])
                listData[index] = str(listData[index])

        for d in loads(context['serialized']):
            #clasify if its an income or expense
            if d['fields']['type'] == 2:
                Selector(d, labelsExpense, dataExpense)
                sum_expense += abs(float(d['fields']['Amount']))
            elif d['fields']['type'] == 1:
                Selector(d, labelsIncome, dataIncome)
                sum_income += abs(float(d['fields']['Amount']))

        context['chartIncome'] = dumps({
            "labels": labelsIncome,
            "default": dataIncome,
        })
        context['chartExpense'] = dumps({
            "labels": labelsExpense,
            "default": dataExpense,
        })
        context['SUM'] = {
            "income": sum_income,
            "expense": sum_expense,
            "balance": sum_income-sum_expense,
        }
        return context

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
        form.fields['description'] = forms.CharField(required=False)
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
        form.fields['description'] = forms.CharField(required=False)
        form.fields['category'].queryset = Category.objects.filter(type__name='Income')
        form.fields['date'] = forms.DateField(widget=DateInput)
        return form

    def form_valid(self, form):
        form.instance.Amount = abs(form.cleaned_data['Amount'])
        form.instance.type = Type.objects.get(name='Income')
        form.instance.user = self.request.user
        return super().form_valid(form)
