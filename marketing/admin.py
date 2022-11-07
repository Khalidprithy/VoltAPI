from django.contrib import admin
from django.utils.html import format_html

from .models import *
# Register your models here.



class Marketingline(admin.StackedInline):
    model = Marketing
    extra = 0


class MarketingModelInline(admin.StackedInline):
    model = MarketingModule
    extra = 0


class MarketingTaskline(admin.StackedInline):
    model = MarketingTask
    extra = 0


@admin.register(MarketingModule)
class MarketingModel(admin.ModelAdmin):
    model = MarketingModule
    list_display = ['startup']
    list_per_page = 15
    inlines = [Marketingline, MarketingTaskline]
    search_fields = ['startup__name__istartswith']