from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return render(request, 'finance/index.html')

def about(request):
    return render(request, 'finance/base.html')