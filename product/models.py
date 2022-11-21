from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from backend.models import Startup, Profile

# Create your models here.

class ProductModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.startup.name + " Product"

def generate_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Product.objects.filter(key=key).exists():
          break  
    return key

class Product(models.Model):
    PHASE_CHOICES = [
        ('I', 'Ideation'),
        ('D', 'Design'),
        ('MVP', 'MVP (Minimum Viable Product)'),
        ('PoC', 'Proof of concept'),
        ('PMF', 'Product Market Fit'),
        ('C', 'Customer Acquisition'),
        ('S', 'Scaling'),
    ]
    PLATFORM_CHOICES = [
        ('D', 'Desktop application'),
        ('S', 'Service'),
        ('I', 'IOS application'),
        ('W', 'Website'),
        ('A', 'Android application'),
        ('H', 'Hardware')
    ]
    KEYWORD_CHOICES = [
        ('E', 'Ecommerce'),
        ('Sm', 'Social media'),
        ('S', 'SaaS'),
        ('T', 'Travel'),
    ]
    key = models.SlugField(editable=False, default=generate_key)
    productModule = models.ForeignKey(ProductModule, on_delete=models.CASCADE, related_name='products')
    productLeader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=50)
    phase = models.CharField(choices=PHASE_CHOICES, max_length=50)
    keyword = models.CharField(choices=KEYWORD_CHOICES, max_length=50)
    completed = models.BooleanField(default=False)
    version = models.CharField(max_length=50, default="0.0.1")
    deployed_link = models.URLField(null=True, blank=True, max_length=200)

    def __str__(self) -> str:
        return self.name + " by " + self.productModule.startup.name + ("Completed" if self.completed else "")

def generate_feature_key():
    length=10
    base = string.ascii_letters+string.digits
    while True:
        key = ''.join(random.choices(base,k=length))
        if not Feature.objects.filter(key=key).exists():
          break  
    return key

class Feature(models.Model):
    key = models.SlugField(editable=False, default=generate_key)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title + self.title

class Image(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    tag = models.CharField(null=True, max_length=50)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    is_ss = models.BooleanField(default=False)
    
class Timeline(models.Model):
    CATE_CHOICES = [
        ('V', 'Version Updated'),
        ('F', 'Feature Added'),
        ('FC', 'Feature Completed'),
        ('P', 'Product Status Changed'),
        ('D', 'Designs Added'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, null=True)
    text = models.CharField(null=True, max_length=50)
    cate = models.CharField(choices=CATE_CHOICES, max_length=50)
