from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=20)
 
    def __str__(self):
        return self.name

class Category(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
 
    def __str__(self):
        return self.name

class Movement(models.Model):
    description = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=19, decimal_places=2)
    datePosted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('finance-home')