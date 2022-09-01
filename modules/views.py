from django.http import HttpResponse
from django.shortcuts import render
from .models import BasicModel


# Create your views here.
def hello(request):
    queryset = BasicModel.objects.values('name', 'idea')

    return HttpResponse(queryset)
