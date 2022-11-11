from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User

from backend.models import Startup, Profile
from strategy.models import *
# Create your models here.


class StrategyModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)

    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Strategy'
    
class Strategy(models.Model):
    CATEGORY_CHOICES = [
        ('M', 'Major'),
        ('m', 'Minor'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    strategyModule = models.ForeignKey(StrategyModule, on_delete=models.CASCADE, parent_link=True,
                                      related_name='strategies')
    strategyTitle = models.CharField(max_length=255)
    strategy = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='M')
    approxStartDate = models.DateField()
    strategyLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    customer = models.TextField()
    features = models.TextField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')
    problemArea = models.TextField()
    uses = models.TextField()

    def __str__(self) -> str:
        return self.strategyTitle + ' Strategy'