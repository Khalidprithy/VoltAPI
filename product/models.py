from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User
from backend.models import Startup, Profile

# Create your models here.

class ProductModule(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.startup.name + " Product"


class Product(models.Model):
    TYPE_CHOICES = [
        ('S', 'Software'),
        ('S', 'Service'),
        ('E', 'Education'),
        ('H', 'Hardware'),
        ('E', 'Electronics'),
    ]
    PHASE_CHOICES = [
        ('I', 'Ideation'),
        ('D', 'Design'),
        ('MVP', 'MVP (Minimum Viable Product)'),
        ('PoC', 'Proof of concept'),
        ('PMF', 'Product Market Fit'),
        ('C', 'Customer Acquisition'),
        ('S', 'Scaling'),
    ]
    productModule = models.ForeignKey(ProductModule, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    product_type = models.CharField(choices=TYPE_CHOICES, max_length=50)
    problemArea = models.TextField()
    phase = models.CharField(choices=PHASE_CHOICES, max_length=50)
    completed = models.BooleanField(default=False)
    version = models.CharField(max_length=50, default="0.0.1")
    deployed_link = models.URLField(null=True, blank=True, max_length=200)

    def __str__(self) -> str:
        return self.name + " by " + self.productModule.startup.name + ("Completed" if self.completed else "")

class ProductDesign(models.Model):
    subname = models.CharField(null=True, max_length=50)
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    designs = models.FileField(null=True, upload_to=None, max_length=100)
    figma = models.URLField(null=True, max_length=200)
    canva = models.URLField(null=True, max_length=200)
    final = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.subname + " for " + self.product.name + ("Final" if self.final else "")
