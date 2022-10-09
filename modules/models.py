from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class BasicModel(models.Model):
    name = models.CharField(max_length=255)
    idea = models.TextField()
    problemArea = models.TextField()
    currentPlayers = models.TextField()
    difference = models.TextField()
    customer = models.TextField()
    revenueQuestion = models.TextField()
    revenueAnswer = models.TextField()
    stage = models.TextField()
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
    basicModel = models.ForeignKey(BasicModel, on_delete=models.SET_NULL, null=True, related_name='profile')
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


class StrategyModel(models.Model):
    basicModel = models.ForeignKey(BasicModel, unique=True, on_delete=models.CASCADE)
    customer = models.TextField()
    problemArea = models.TextField()
    uses = models.TextField()

    class Meta:
        ordering = ['basicModel']

    def __str__(self) -> str:
        return self.basicModel.name + ' Strategy'


class Up(models.Model):
    ups = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE, related_name='ups')

    def __str__(self) -> str:
        return self.ups


class Segment(models.Model):
    segments = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE, related_name='segments')

    def __str__(self) -> str:
        return self.strategyModel.basicModel.name + ' Segment'


class Partner(models.Model):
    partners = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE, related_name='partners')

    def __str__(self) -> str:
        return self.strategyModel.basicModel.name + ' Partner'


class Influencer(models.Model):
    influencers = models.TextField()
    how = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE, related_name='influencers')

    def __str__(self) -> str:
        return self.strategyModel.basicModel.name + ' Influencer'


class Strategy(models.Model):
    CATEGORY_CHOICES = [
        ('M', 'Major'),
        ('m', 'Minor'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE, parent_link=True,
                                      related_name='strategies')
    strategyTitle = models.CharField(max_length=255)
    strategy = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='M')
    approxStartDate = models.DateField()
    strategyLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    Customer = models.TextField()
    features = models.TextField()
    description = models.TextField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')

    def __str__(self) -> str:
        return self.strategyTitle + ' Strategy'


class ResearchModel(models.Model):
    basicModel = models.ForeignKey(BasicModel, on_delete=models.CASCADE, unique=True)
    additionalArticles = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['basicModel']

    def __str__(self) -> str:
        return self.basicModel.name + ' Research'


class Research(models.Model):
    CATEGORY_CHOICES = [
        ('P', 'Primary'),
        ('S', 'Secondary'),
    ]
    researchModel = models.ForeignKey(ResearchModel, on_delete=models.CASCADE, related_name='researches')
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    researchTitle = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='P')
    researchLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    researchTask = models.TextField()
    conclusion = models.TextField()
    researchArtifacts = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.researchTitle


class MarketingModel(models.Model):
    basicModel = models.ForeignKey(BasicModel, unique=True, on_delete=models.CASCADE)
    LinkedIn = models.TextField()
    Facebook = models.TextField()
    Twitter = models.TextField()
    Instagram = models.TextField()
    Youtube = models.TextField()

    class Meta:
        ordering = ['basicModel']

    def __str__(self) -> str:
        return self.basicModel.name + ' Marketing'


class Marketing(models.Model):
    TYPE_CHOICES = [
        ('M', 'Major'),
        ('m', 'Minor'),
    ]
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    marketingModel = models.ForeignKey(MarketingModel, on_delete=models.CASCADE)
    strategy = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)
    marketingTitle = models.TextField()
    marketingLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')

    def __str__(self) -> str:
        return self.marketingTitle


class MarketingTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    marketing = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    marketingModel = models.ForeignKey(MarketingModel, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()

    def __str__(self) -> str:
        return self.marketing.marketingTitle + ' Task'


class SalesModel(models.Model):
    basicModel = models.ForeignKey(BasicModel, unique=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['basicModel']

    def __str__(self) -> str:
        return self.basicModel.name + ' Sales'


class Sale(models.Model):
    TYPE_CHOICES = [
        ('M', 'Major'),
        ('m', 'Minor'),
    ]
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    SUCCESS_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    salesModel = models.ForeignKey(SalesModel, on_delete=models.CASCADE)
    strategy = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)
    salesTitle = models.TextField()
    salesLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')

    def __str__(self) -> str:
        return self.salesTitle


class SalesTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    salesModel = models.ForeignKey(SalesModel, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()

    def __str__(self) -> str:
        return self.sales.salesTitle + ' Task'
