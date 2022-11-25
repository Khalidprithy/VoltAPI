from django.contrib import admin
from django.utils.html import format_html

from .models import *
# Register your models here.

class Featureline(admin.StackedInline):
    model = Feature
    extra = 0

class Productline(admin.StackedInline):
    model = Product
    extra = 0

class ProductModelInline(admin.StackedInline):
    model = ProductModule
    extra = 0

@admin.register(ProductModule)
class ProductModel(admin.ModelAdmin):
    model = ProductModule
    list_display = ['startup']
    list_per_page = 15
    inlines = [Productline]
    search_fields = ['startup__name__istartswith']