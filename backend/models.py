from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class Startup(models.Model):
    name = models.CharField(max_length=255)
    founded = models.DateField(auto_now=False, auto_now_add=False, null=True)
    idea = models.TextField()
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

    class Meta:
        ordering = ['name', '-points']

    def __str__(self) -> str:
        return self.name

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


