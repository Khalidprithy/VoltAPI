from django.contrib import admin
from django.utils.html import format_html

from .models import *
# Register your models here.


class Saleline(admin.StackedInline):
    model = Sale
    extra = 0


class SalesTaskline(admin.StackedInline):
    model = SalesTask
    extra = 0


@admin.register(SalesModule)
class SalesModel(admin.ModelAdmin):
    model = SalesModule
    list_display = ['startup']
    list_per_page = 15
    inlines = [Saleline, SalesTaskline]
    search_fields = ['startup__name__istartswith']