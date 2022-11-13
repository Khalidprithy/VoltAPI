from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class CreateStrategyView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup = request.GET.get('startup')
        strategyModule = StrategyModule.objects.get(startup=startup)
        strategy = Strategy.objects.create(
            CATEGORY_CHOICES = data.get("CATEGORY_CHOICES"),
            SUCCESS_CHOICES = data.get("SUCCESS_CHOICES"),
            strategyTitle = data.get("strategyTitle"),
            strategy = data.get("strategy"),
            category = data.get("category"),
            approxStartDate = data.get("approxStartDate"),
            strategyLeader = data.get("strategyLeader"),
            customer = data.get("customer"),
            features = data.get("features"),
            success = data.get("success"),
            problemArea = data.get("problemArea"),
            uses = data.get("uses")
        )
        strategy.strategyModule = strategyModule
        return Response({"message": "done"})

class GetStrategyView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        strategyModule = StrategyModule.objects.get(startup=startup)
        your_strategies = Strategy.objects.filter(strategyModule=strategyModule)
        your_strategies_data = StrategySerializer(your_strategies, many=True).data
        payload = {
            'your_strategies': your_strategies_data
        }
        return Response(payload, status=status.HTTP_200_OK)