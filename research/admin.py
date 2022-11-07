from django.contrib import admin
from django.utils.html import format_html

from .models import *
# Register your models here.


class ResearchModelInline(admin.StackedInline):
    model = ResearchModule
    extra = 0


class Researchline(admin.StackedInline):
    model = Research
    extra = 0


@admin.register(ResearchModule)
class ResearchModel(admin.ModelAdmin):
    model = ResearchModule
    list_display = ['startup']
    list_per_page = 15
    inlines = [Researchline]
    search_fields = ['startup__name__istartswith']
