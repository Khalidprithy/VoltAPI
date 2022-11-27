from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from backend.models import Startup, Profile
from strategy.models import *
from marketing.models import *
import string
import random
from ckeditor.fields import RichTextField
# Create your models here.



class ResearchModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    head = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    volts = models.IntegerField(default=0)

    class Meta:
        ordering = ['startup']

    def __str__(self) -> str:
        return self.startup.name + ' Research'

def generate_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Marketing.objects.filter(key=key).exists():
          break  
    return key

class Research(models.Model):
    CATEGORY_CHOICES = [
        ('B', 'Brief'),
        ('I', 'Image/Poster'),
        ('V', 'Video'),
        ('R', 'Research'),
    ]
    STATUS_CHOICES = [
        ('C', 'Completed'),
        ('D', 'Draft'),
        ('T', 'Task')
    ]
    key = models.SlugField(editable=False, default=generate_key)
    researchModule = models.ForeignKey(ResearchModule, on_delete=models.CASCADE, related_name='researches')
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, null=True)
    task = models.TextField(unique=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='P')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, null=True)
    conclusion = RichTextField(null=True)
    img = models.ImageField(null=True, upload_to="startup/content/img")
    video = models.FileField(upload_to="startup/content/video", null=True)
    volts = models.IntegerField(default=5)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='T')

    def __str__(self) -> str:
        return self.task