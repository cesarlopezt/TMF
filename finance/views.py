from django.shortcuts import render
from .models import Movement
from django.views.generic import ListView, DetailView, CreateView


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
   ordering = ['-datePosted']

# class MovementDetailView(DetailView):
#    model = Movement
class MovementCreateView(CreateView):
   model = Movement
   fields = ['description', 'Amount']

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)