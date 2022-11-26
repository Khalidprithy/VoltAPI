from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from research.serializers import *
from research.models import *

# Create your views here.
class CreateMarketingView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup_key = data.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        marketingModule = MarketingModule.objects.get(startup=startup)
        strategy = Strategy.objects.get(strategyTitle=data.get("strategyTitle"))
        marketing = Marketing.objects.create(
            marketingModule=marketingModule,
            strategy=strategy,
            marketingTitle = data.get("marketingTitle"),
            marketingLeader = data.get("marketingLeader"),
            type = data.get("type"),
            status = data.get("status"),
            description = data.get("description"),
            startDate = data.get("startDate"),
            endDate = data.get("endDate"),
            success = data.get("success")
        )
        return Response({"message": "done"})

class GetMarketingStrategiesView(APIView):
    def get(self, request, format=None):
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        marketingModule = MarketingModule.objects.get(startup=startup)
        your_marketing = Marketing.objects.filter(marketingModule=marketingModule)
        your_marketing_data = MarketingSerializer(your_marketing, many=True).data
        payload = {
            'strategies': your_marketing_data
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetMarketingStrategyView(APIView):
    def get(self, request, format=None):
        slug = request.GET.get("slug")
        marketing = Marketing.objects.filter(slug=slug)
        if marketing.exists():
            marketing = marketing.first()
            linkedin, instagram, youtube = []
            content = PublicResearchSerializer(Research.objects.filter(marketing=marketing), many=True).data
            payload = {
                "details": details,
                "linkedin": linkedin,
                "instagram": instagram,
                "youtube": youtube,
                "content": content
            }
            return Response(payload, status=status.HTTP_200_OK)
        return Response({"message": "invalid slug!"}, status=status.HTTP_404_NOT_FOUND)
            
