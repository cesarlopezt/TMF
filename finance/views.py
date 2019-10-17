from django.shortcuts import render
from .models import Movement


def home(request):
   # context = {
   #    'Movements' : Movement.objects.all()
   # }
   return render(request, 'finance/userMainPage.html',{'title': 'Main Page'})

def about(request):
    return render(request, 'finance/base.html')