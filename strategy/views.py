from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from marketing.models import *
from strategy.models import *
from research.models import *
from sales.models import *


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

class GetStrategiesView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        strategyModule = StrategyModule.objects.get(startup=startup)
        your_strategies = Strategy.objects.filter(strategyModule=strategyModule)
        strategies_ = []
        for strategy in your_strategies:
            strategy_ = {}
            strategy_["details"] = StrategySerializer(strategy).data
            strategy_["subs"] = {
                "marketing": len(Marketing.objects.filter(strategy=strategy)),
                "sales": len(Sales.objects.filter(strategy=strategy)),
                "research": len(Research.objects.filter(strategy=strategy))
            }
            strategies_.append(strategy_)
        payload = {
            'your_strategies': strategies_
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetStrategyView(APIView):
    def get(self, request, format=None):
        startup_key = models.request.GET.get("startup_key")
        startup = Startup.objects.get(people=user, key=startup_key)
        strategy_module = StrategyModule.objects.get(startup=startup)
        strategy = Strategy.objects.filter(strategyModule=strategy_module)
        if strategy.exists():
            strategy = strategy.first()
            marketing_sub = Marketing.objects.filter(strategy=strategy)
            sales_sub = Sales.objects.filter(strategy=strategy)
            research_sub = Research.objects.filter(strategy=strategy)
            sub = {
                "sales": sales_sub,
                "marketing": marketing_sub,
                "research": research_sub,
            }
            payload = {
                "strategy": StrategySerializer(strategy).data,
                "sub_strategies": sub
            }
            return Response(payload, status=status.HTTP_200_OK)
        return Response({"message": "not found!"}, status=status.HTTP_404_NOT_FOUND)