from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class BasicModel(models.Model):
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


class User(models.Model):
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    yearOfGraduation = models.DateField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    founder = models.BooleanField(default=False)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    joined_on = models.DateField(auto_now_add=True)
    basicModel = models.ForeignKey(BasicModel, on_delete=models.SET_NULL, null=True)


class StrategyModel(models.Model):
    baseModel = models.ForeignKey(BasicModel, on_delete=models.CASCADE)
    customer = models.TextField()
    problemArea = models.TextField()
    uses = models.TextField()


class Ups(models.Model):
    ups = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)


class AddCustomers(models.Model):
    addCustomers = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)


class Segments(models.Model):
    segments = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)


class Partners(models.Model):
    partners = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)


class Influencers(models.Model):
    influencers = models.TextField()
    how = models.TextField()
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)


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
    strategyModel = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)
    strategy = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='M')
    approxStartDate = models.DateField()
    strategyLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Customer = models.TextField()
    features = models.TextField()
    description = models.TextField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')


class ResearchModel(models.Model):
    baseModel = models.ForeignKey(BasicModel, on_delete=models.CASCADE)
    additionalArticles = models.TextField()


class Research(models.Model):
    CATEGORY_CHOICES = [
        ('P', 'Primary'),
        ('S', 'Secondary'),
    ]
    researchModel = models.ForeignKey(ResearchModel, on_delete=models.CASCADE)
    strategy = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)
    researchTitle = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default='P')
    researchLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    researchTask = models.TextField()
    conclusion = models.TextField()
    researchArtifacts = models.TextField()


class MarketingModel(models.Model):
    baseModel = models.ForeignKey(BasicModel, on_delete=models.CASCADE)
    LinkedIn = models.TextField()
    Facebook = models.TextField()
    Twitter = models.TextField()
    Instagram = models.TextField()
    Youtube = models.TextField()


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
    marketingLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')


class MarketingTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    marketing = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()


class SalesModel(models.Model):
    baseModel = models.ForeignKey(BasicModel, on_delete=models.CASCADE)


class Sales(models.Model):
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
    salesLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='M')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='A')
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    success = models.CharField(choices=SUCCESS_CHOICES, max_length=1, default='M')


class SalesTask(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    task = models.TextField()
    taskLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1, default='A')
    description = models.TextField()
    outcome = models.TextField()
