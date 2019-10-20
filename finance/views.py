from django.shortcuts import render
from .models import Movement
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


# def home(request):
#    context = {
#       'title': 'Main Page',
#       'Movements' : Movement.objects.all()
#    }
#    return render(request, 'finance/MainPage.html',context)

class MovementListView(ListView):
   model = Movement
   template_name = "finance/MainPage.html"
   context_object_name = 'Movements'
   ordering = ['-date']

# class MovementDetailView(DetailView):
#    model = Movement

#DEFINE THE DATE INPUT THAT I WANTED
class DateInput(forms.DateInput):
   input_type = 'date'

class MovementCreateView(LoginRequiredMixin, CreateView):
   model = Movement
   fields = ['description', 'Amount', 'date']
   
   def get_form(self, form_class = None):
      form = super(MovementCreateView, self).get_form(form_class)
      form.fields['date'] = forms.DateField(widget=DateInput)
      return form

   def form_valid(self, form):
      # print(self.request.user.value)
      form.instance.user = self.request.user
      return super().form_valid(form)