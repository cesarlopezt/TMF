from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Movement(models.Model):
    description = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=19, decimal_places=4)
    datePosted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

