from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User

from backend.models import Startup, Profile
from strategy.models import *
from django.utils.text import slugify

import string
import random
# Create your models here.


class StrategyModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    head = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    volts = models.IntegerField(default=0)

    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Strategy'

def generate_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Startup.objects.filter(key=key).exists():
          break  
    return key 

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
    slug = models.SlugField(null=True, max_length=300, unique=True)
    strategyModule = models.ForeignKey(StrategyModule, on_delete=models.CASCADE, parent_link=True,
                                      related_name='strategies')
    strategyTitle = models.CharField(max_length=255)
    strategy = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='M')
    approxStartDate = models.DateField()
    strategyLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    customer = models.TextField()
    features = models.TextField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='L')
    problemArea = models.TextField()
    uses = models.TextField(null=True)
    points = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.strategyTitle + ' Strategy'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.strategyTitle)
        super(Strategy, self).save(*args, **kwargs)

class StrategyResult(models.Model):
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    remarks = models.TextField()
    matrix_met = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='L')
    report = models.FileField(upload_to=None, null=True, blank=True)
    points_alloted = models.IntegerField(default=10)
    confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.strategy.strategyTitle + ' Strategy' + [' Confirmed', ' Under review'][self.confirmed]