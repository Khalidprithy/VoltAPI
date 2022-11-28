from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from research.serializers import *
from research.models import *
from datetime import datetime

# Create your views here.
class CreateMarketingView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup_key = data.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        marketingModule = MarketingModule.objects.get(startup=startup)
        strategy = Strategy.objects.get(slug=data.get("strategy_slug"))
        leader = User.objects.get(username=data.get("marketingLeader"))

        startDate = datetime.strptime(data.get("startDate"), '%Y-%m-%d').date()
        endDate = datetime.strptime(data.get("endDate"), '%Y-%m-%d').date()

        marketing = Marketing.objects.create(
            marketingModule=marketingModule,
            strategy=strategy,
            marketingTitle = data.get("marketingTitle"),
            marketingLeader = leader,
            major = data.get("major"),
            status = data.get("status"),
            description = data.get("description"),
            startDate = startDate,
            endDate = endDate,
        )
        for platform in Platform.objects.filter(marketing=marketingModule):
            Social.objects.create(marketing=marketing, platform=platform)
        return Response({"message": "done"})

def SetSocialGoalsView(APIView):
    def post(self, request, format=None):
        data = request.data
        marketing_key = data.get('marketing_key')
        for social in Social.objects.filter(marketing__key=marketing_key):
            social_data = data.get(social.platform.media)
            social.expected_posts = social_data.get('expected_posts')
            social.low = social_data.get('low')
            social.mid = social_data.get('mid')
            social.high = social_data.get('high')
            social.points = social_data.get('points')
            social.save(update_fields=['expected_posts', 'low', 'mid', 'high', 'points'])
        return Response({"message": "socials updated!"}, status=status.HTTP_200_OK)

def add_marketing(strategies):
    payload = {
        'major': [],
        'minor': [],
    }
    for strategy in strategies:
        strategy_ = {}
        strategy_["details"] = MarketingSerializer(strategy).data
        strategy_["subs"] = {
            "youtube": [],
            "instagram": [],
            "linkedin": [],
        }
        if strategy.major:
            payload['major'].append(strategy_)
        payload['minor'].append(strategy_)
    return payload

def get_all_marketing(startup):
    strats = Marketing.objects.filter(marketingModule__startup=startup)
    inprogress = []
    completed = []
    for strat in strats:
        if strat.is_completed():
            completed.append(strat)
        else :
            inprogress.append(strat)
    return inprogress, completed

class GetMarketingStrategiesView(APIView):
    def get(self, request, format=None):
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        inprogress, completed = get_all_marketing(startup)
        tasks = [] # All socials posts
        socials = Platform.objects.filter(marketing__startup=startup)

        payload = {
            'inprogress': add_marketing(inprogress),
            'completed': add_marketing(completed),
            'tasks': tasks,
            'socials': socials
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetMarketingStrategyView(APIView):
    def get(self, request, format=None):
        slug = request.GET.get("slug")
        marketing = Marketing.objects.filter(slug=slug)
        if marketing.exists():
            marketing = marketing.first()
            linkedin, instagram, youtube = []
            content = PublicResearchSerializer(Research.objects.filter(strategy=marketing.strategy), many=True).data
            payload = {
                "details": details,
                "linkedin": linkedin,
                "instagram": instagram,
                "youtube": youtube,
                "content": content
            }
            return Response(payload, status=status.HTTP_200_OK)
        return Response({"message": "invalid slug!"}, status=status.HTTP_404_NOT_FOUND)
            
