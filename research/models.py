from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from backend.models import Startup, Profile
from strategy.models import *
import string
import random
# Create your models here.



class ResearchModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    additionalArticles = models.TextField(null=True, blank=True)
    head = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    volts = models.IntegerField(default=0)

    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Research'


class Research(models.Model):
    CATEGORY_CHOICES = [
        ('P', 'Primary'),
        ('S', 'Secondary'),
    ]
    researchModule = models.ForeignKey(ResearchModule, on_delete=models.CASCADE, related_name='researches')
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    researchTitle = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='P')
    researchLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    researchTask = models.TextField()
    conclusion = models.TextField()
    researchArtifacts = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.researchTitle