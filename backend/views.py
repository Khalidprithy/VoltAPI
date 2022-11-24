from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from .models import *
from .serializers import *
from rest_framework.views import APIView
import random
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import json
import datetime
from rest_framework import status

from marketing.models import *
from strategy.models import *
from research.models import *
from sales.models import *
from product.models import *

# Create your views here.
class StartupViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = StartupSerializer
    queryset = Startup.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        baseModel = Startup.objects.get(profile=profile)
        if request.method == 'GET':
            serializer = StartupSerializer(baseModel)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = StartupSerializer(baseModel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class PublicStartupViewSet(ReadOnlyModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = PublicStartupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'users__first_name', 'users__last_name']

    def get_serializer_context(self):
        return {'request': self.request}


class ProfileViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get', 'put'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        if request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class PublicProfileViewSet(ModelViewSet):
    serializer_class = PublicProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'user__last_name']

    def get_serializer_context(self):
        return {'request': self.request}


class CreateStartupView(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        user = User.objects.get(username=username)
        startup = Startup.objects.create(
            name=data.get("name"),
            founded=data.get("founded"),
            idea=data.get("idea"),
            problemArea=data.get("problemArea"),
            currentPlayers=data.get("currentPlayers"),
            difference=data.get("difference"),
            customer=data.get("customer"),
            revenue1=data.get("revenue1"),
            revenue2=data.get("revenue2"),
            stage=data.get("stage"),
            market=data.get("market"),
            website=data.get("website"),
            registered=data.get("registered")
        )
        if data.get("is_founder"):
            startup.mobs.add(user)
        else :
            startup.people.add(user)
        # configuring the modules 
        StrategyModule.objects.create(startup=startup)
        MarketingModule.objects.create(startup=startup)
        ResearchModule.objects.create(startup=startup)
        SalesModule.objects.create(startup=startup)
        ProductModule.objects.create(startup=startup)

        emails = data.get('emails').split(',')
        # send_invite_mails(emails)
        # send_join_mail(user.email)

        return Response({"message": "done"}, status=status.HTTP_201_CREATED)

class GetStartupsView(APIView):
    def get(self, request, format=None):
        username = request.GET.get('username')
        user = User.objects.get(username=username)
        your_startups = Startup.objects.filter(people=user)
        all_startups = Startup.objects.all().exclude(people=user)
        
        your_startups_data = []
        for startup in your_startups:
            startup_ = {}
            startup_['details'] = PublicStartupSerializer(startup).data
            startup_['members'] = len(startup.people.all())
            your_startups_data.append(startup_)

        all_startups_data = []
        for startup in all_startups:
            startup_ = {}
            startup_['details'] = PublicStartupSerializer(startup).data
            startup_['members'] = len(startup.people.all())
            all_startups_data.append(startup_) 

        payload = {
            'your_startups': your_startups_data,
            'all_startups': all_startups_data
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetStartupView(APIView):
    def get(self, request, format=None):
        username = request.GET.get('username')
        user = User.objects.get(username=username)
        startup_key = models.request.GET.get("startup_key")
        startup = Startup.objects.filter(people=user, key=startup_key)
        if startup.exists():
            startup = startup.first()
            MarketingVolts = MarketingModule.objects.get(startup=startup).volts
            StrategyVolts = StrategyModule.objects.get(startup=startup).volts
            ResearchVolts = ResearchModule.objects.get(startup=startup).volts
            ProductVolts = ProductModule.objects.get(startup=startup).volts
            SalesVolts = SalesModule.objects.get(startup=startup).volts
            total_points = MarketingVolts+SalesVolts+ResearchVolts+ProductVolts+StrategyVolts
            stats = {
                "strategy": StrategyVolts/total_points*100,
                "marketing": MarketingVolts/total_points*100,
                "sales": SalesVolts/total_points*100,
                "product": ProductVolts/total_points*100,
                "research": StrategyVolts/total_points*100,
            }
            payload = {
                "details": StartupSerializer(startup).data,
                "stats": stats,
            }
            return Response(payload, status=status.HTTP_200_OK)
        return Response({"message": "not found!"}, staus=status.HTTP_404_NOT_FOUND)