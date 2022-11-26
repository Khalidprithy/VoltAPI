from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from backend.models import Startup, Profile
from strategy.models import *
import string
import random
# Create your models here.


class SalesModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    head = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    volts = models.IntegerField(default=0)
    
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
    salesModule = models.ForeignKey(SalesModule, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
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

    def is_completed(self) -> bool:
        return True

class SalesTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    salesModule = models.ForeignKey(SalesModule, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()

    def __str__(self) -> str:
        return self.sales.salesTitle + ' Task'