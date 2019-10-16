from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='finance-home'),
    path('about/', views.about, name='finance-about'),
]