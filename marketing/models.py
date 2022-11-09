from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from backend.models import Startup, Profile
from strategy.models import *
# Create your models here.



class MarketingModule(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    LinkedIn = models.TextField()
    Facebook = models.TextField()
    Twitter = models.TextField()
    Instagram = models.TextField()
    Youtube = models.TextField()

    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Marketing'


class Marketing(models.Model):
    TYPE_CHOICES = [
        ('M', 'Major'),
        ('m', 'Minor'),
    ]
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    marketingModule = models.ForeignKey(MarketingModule, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    marketingTitle = models.TextField()
    marketingLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')

    def __str__(self) -> str:
        return self.marketingTitle


class MarketingTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    marketing = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    marketingModel = models.ForeignKey(MarketingModule, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()

    def __str__(self) -> str:
        return self.marketing.marketingTitle + ' Task'
