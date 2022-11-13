from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class CreateMarketingView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup = request.GET.get('startup')
        marketingModule = MarketingModule.objects.get(startup=startup)
        marketing = Marketing.objects.create(
            TYPE_CHOICES = data.get("TYPE_CHOICES"),
            SUCCESS_CHOICES = data.get("SUCCESS_CHOICES"),
            STATUS_CHOICES = data.get("STATUS_CHOICES"),
            marketingTitle = data.get("marketingTitle"),
            marketingLeader = data.get("marketingLeader"),
            type = data.get("type"),
            status = data.get("status"),
            description = data.get("description"),
            startDate = data.get("startDate"),
            endDate = data.get("endDate"),
            success = data.get("success")
        )
        marketing.marketingModule = marketingModule
        return Response({"message": "done"})

class GetStrategyView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        marketingModule = MarketingModule.objects.get(startup=startup)
        your_marketing = Marketing.objects.filter(marketingModule=marketingModule)
        your_marketing_data = MarketingSerializer(your_marketing, many=True).data
        payload = {
            'your_marketing': your_marketing_data
        }
        return Response(payload, status=status.HTTP_200_OK)