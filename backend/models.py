from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from django.db import models

import string
import random
# Create your models here.
def generate_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Startup.objects.filter(key=key).exists():
          break  
    return key

class Startup(models.Model):
    key = models.SlugField(editable=False, default=generate_key)
    logo = models.ImageField(null=True, upload_to="startup/logo")
    name = models.CharField(max_length=255, unique=True)
    vision = models.CharField(null=True, max_length=100, unique=True)
    founded = models.CharField(null=True, max_length=50)
    idea = models.TextField(unique=True)
    problemArea = models.TextField()
    currentPlayers = models.TextField()
    difference = models.TextField()
    customer = models.TextField()
    revenue1 = models.TextField()
    revenue2 = models.TextField(null=True)
    stage = models.TextField()
    market = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    people = models.ManyToManyField(User, related_name="people", blank=True)
    website = models.URLField(null=True, max_length=200)
    registered = models.BooleanField(default=False)
    mobs = models.ManyToManyField(User, related_name="mobs")

    class Meta:
        ordering = ['name', '-points']

    def __str__(self) -> str:
        return self.name

def generate_idea_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Startup.objects.filter(key=key).exists():
          break  
    return key

class Idea(models.Model):
    key = models.SlugField(default=generate_idea_key, editable=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    idea = models.TextField(null=False, unique=True)
    starred = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    support = models.IntegerField(default=1)
    want_to_work = models.ManyToManyField(User, related_name="want_to_work")

    def __str__(self):
        return self.idea

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    ROLE_CHOICES = [
        ('T', 'Tech'),
        ('S', 'Sales'),
        ('M', 'Marketing'),
        ('L', 'Legal & Admin'),
        ('O', 'Operations'),
    ]
    phone_number = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    yearOfGraduation = models.CharField(max_length=4)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    founder = models.BooleanField(default=False)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    joined_on = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    startup = models.ForeignKey(Startup, on_delete=models.SET_NULL, null=True, related_name='profile')
    image = models.ImageField(upload_to='profile/images', default='profile/images/default.png')

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def __str__(self) -> str:
        return f'{self.first_name() + " " + self.last_name() + " (founder)"}' if self.founder else self.first_name() + " " + self.last_name()


class Up(models.Model):
    ups = models.TextField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='ups')

    def __str__(self) -> str:
        return self.ups


class Segment(models.Model):
    segments = models.TextField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='segments')

    def __str__(self) -> str:
        return self.startup.startup.name + ' Segment'


class Partner(models.Model):
    partners = models.TextField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='partners')

    def __str__(self) -> str:
        return self.startup.startup.name + ' Partner'


class Influencer(models.Model):
    influencers = models.TextField()
    how = models.TextField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='influencers')

    def __str__(self) -> str:
        return self.startup.startup.name + ' Influencer'


class Meetup(models.Model):
    IMP_CHOICES = [
        ('I', 'Important'),
        ('D', 'Discussion'),
        ('N', 'Normal'),
        ('D', 'Daily'),
        ('O', 'Optional'),
    ]
    title = models.CharField(null=False, max_length=50)
    desc = models.TextField()
    link = models.URLField(null=False, max_length=200)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    instant = models.BooleanField(default=False)
    mobs_only = models.BooleanField(default=False)
    importance = models.CharField(null=False, max_length=50, choices=IMP_CHOICES)

    def __str__(self) -> str:
        return self.startup + ' meetup for ' + self.importance + self.title