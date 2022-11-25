from django.contrib import admin
from django.utils.html import format_html

from .models import *
from django.contrib.auth.admin import UserAdmin
from strategy.admin import *
from research.admin import *
from marketing.admin import *
from sales.admin import *
from product.admin import *

# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'startup', 'founder','thumbnail']
    readonly_fields = ['thumbnail']
    list_per_page = 15
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    autocomplete_fields = ['startup']

    def thumbnail(self, instance):
        if instance.image:
            return format_html(f'<img src="{instance.image.url}" width="50" height="50" object-fit:"cover" style="border-radius: 50%;" />')



@admin.register(Startup)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'points_status', 'created_at']
    list_per_page = 15
    inlines = [StrategyModelInline, ResearchModelInline, MarketingModelInline, ProductModelInline, StrategyModelInline]
    search_fields = ['name__istartswith']

    @admin.display(ordering='points')
    def points_status(self, Startup):
        if Startup.points < 400:
            return '🔴'
        elif Startup.points < 700:
            return '🟡'
        else:
            return '🟢'



class UpInline(admin.StackedInline):
    model = Up
    extra = 0


class Segmentline(admin.StackedInline):
    model = Segment
    extra = 0


class Partnerline(admin.StackedInline):
    model = Partner
    extra = 0


class Influencerline(admin.StackedInline):
    model = Influencer
    extra = 0



