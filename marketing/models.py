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

class Social(models.Model):
    SOCIAL_CHOICES = [
        ('L', 'LinkedIn'),
        ('B', 'Blogs'),
        ('F', 'Facebook'),
        ('T', 'Twitter'),
        ('I', 'Instagram'),
        ('Y', 'Youtube'),
        ('R', 'Reddit'),
        ('O', 'Offline')
    ]
    marketing = models.ForeignKey(MarketingModule, on_delete=models.CASCADE)
    social = models.CharField(choices=SOCIAL_CHOICES, max_length=50)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL)
    org_social_link = models.URLField(null=True, max_length=200)
    configured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.marketing.startup + " " + self.social

def generate_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Marketing.objects.filter(key=key).exists():
          break  
    return key

class Marketing(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    key = models.SlugField(editable=False, default=generate_key)
    marketingModule = models.ForeignKey(MarketingModule, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    marketingTitle = models.TextField()
    marketingLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    major = models.BooleanField(default=True)
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
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()
    points = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.marketing.marketingTitle + ' Task'
