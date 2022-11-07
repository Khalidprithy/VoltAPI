from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from backend.models import Startup, Profile
from strategy.models import *
# Create your models here.


class SalesModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Sales'


class Sale(models.Model):
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
    salesModel = models.ForeignKey(SalesModule, on_delete=models.CASCADE)
    strategy = models.ForeignKey(StrategyModule, on_delete=models.CASCADE)
    salesTitle = models.TextField()
    salesLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')

    def __str__(self) -> str:
        return self.salesTitle


class SalesTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    salesModel = models.ForeignKey(SalesModule, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()

    def __str__(self) -> str:
        return self.sales.salesTitle + ' Task'