from django.contrib import admin
from django.utils.html import format_html

from .models import *
# Register your models here.

class StrategyModelInline(admin.StackedInline):
    model = StrategyModule
    extra = 0


class StrategyInline(admin.StackedInline):
    model = Strategy
    extra = 0


@admin.register(StrategyModule)
class StrategyModel(admin.ModelAdmin):
    model = StrategyModule
    list_display = ['startup']
    list_per_page = 15
    search_fields = ['startup__name__istartswith']

