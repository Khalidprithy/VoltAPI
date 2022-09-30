from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'basicModel', 'founder']
    list_per_page = 15
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    autocomplete_fields = ['basicModel']


class StrategyModelInline(admin.StackedInline):
    model = models.StrategyModel
    extra = 0


class ResearchModelInline(admin.StackedInline):
    model = models.ResearchModel
    extra = 0


class MarketingModelInline(admin.StackedInline):
    model = models.MarketingModel
    extra = 0


@admin.register(models.BasicModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'points_status', 'created_at']
    list_per_page = 15
    inlines = [StrategyModelInline, ResearchModelInline, MarketingModelInline]
    search_fields = ['name__istartswith']

    @admin.display(ordering='points')
    def points_status(self, BasicModel):
        if BasicModel.points < 400:
            return '🔴'
        elif BasicModel.points < 700:
            return '🟡'
        else:
            return '🟢'


class StrategyInline(admin.StackedInline):
    model = models.Strategy
    extra = 0


class UpInline(admin.StackedInline):
    model = models.Up
    extra = 0


class Segmentline(admin.StackedInline):
    model = models.Segment
    extra = 0


class Partnerline(admin.StackedInline):
    model = models.Partner
    extra = 0


class Influencerline(admin.StackedInline):
    model = models.Influencer
    extra = 0


@admin.register(models.StrategyModel)
class StrategyModel(admin.ModelAdmin):
    model = models.StrategyModel
    list_display = ['basicModel']
    list_per_page = 15
    inlines = [StrategyInline, UpInline, Segmentline, Partnerline, Influencerline]
    search_fields = ['basicModel__name__istartswith']


class Researchline(admin.StackedInline):
    model = models.Research
    extra = 0


@admin.register(models.ResearchModel)
class ResearchModel(admin.ModelAdmin):
    model = models.ResearchModel
    list_display = ['basicModel']
    list_per_page = 15
    inlines = [Researchline]
    search_fields = ['basicModel__name__istartswith']


class Marketingline(admin.StackedInline):
    model = models.Marketing
    extra = 0


class MarketingTaskline(admin.StackedInline):
    model = models.MarketingTask
    extra = 0

@admin.register(models.MarketingModel)
class MarketingModel(admin.ModelAdmin):
    model = models.MarketingModel
    list_display = ['basicModel']
    list_per_page = 15
    inlines = [Marketingline, MarketingTaskline]
    search_fields = ['basicModel__name__istartswith']


class Saleline(admin.StackedInline):
    model = models.Sale
    extra = 0


class SalesTaskline(admin.StackedInline):
    model = models.SalesTask
    extra = 0


@admin.register(models.SalesModel)
class SalesModel(admin.ModelAdmin):
    model = models.SalesModel
    list_display = ['basicModel']
    list_per_page = 15
    inlines = [Saleline, SalesTaskline]
    search_fields = ['basicModel__name__istartswith']