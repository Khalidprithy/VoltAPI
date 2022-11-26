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
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        strategyModule = StrategyModule.objects.get(startup=startup)
        strategy = Strategy.objects.create(
            strategyModule = strategyModule,
            strategyTitle = data.get("strategyTitle"),
            strategy = data.get("strategy"),
            category = data.get("category"),
            approxStartDate = data.get("approxStartDate"),
            strategyLeader = data.get("strategyLeader"),
            customer = data.get("customer"),
            features = data.get("features"),
            success_low = data.get("success_low"),
            success_mid = data.get("success_mid"),
            success_high = data.get("success_high"),
            problemArea = data.get("problemArea"),
            uses = data.get("uses")
        )
        return Response({"message": "done"})

def add_strategies(strategies):
    payload = {
        'major': [],
        'minor': [],
    }
    for strategy in strategies:
        strategy_ = {}
        strategy_["details"] = StrategySerializer(strategy).data
        strategy_["subs"] = {
            "marketing": len(Marketing.objects.filter(strategy=strategy)),
            "sales": len(Sales.objects.filter(strategy=strategy)),
            "research": len(Research.objects.filter(strategy=strategy)),
        }
        if strategy.category=="M":
            payload['major'].append(strategy_)
        payload['minor'].append(strategy_)
    return payload

def get_all_strategies(startup):
    strats = Strategy.objects.filter(strategyModule__startup=startup)
    inprogress = []
    completed = []
    closed = []
    for strat in strats:
        if StrategyResult.objects.filter(strategy=strat).exists():
            closed.append(strat)
        elif strat.is_completed():
            completed.append(strat)
        else :
            inprogress.append(strat)
    return inprogress, completed, closed

class GetStrategiesView(APIView):
    def get(self, request, format=None):
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        inprogress, completed, closed = get_all_strategies(startup)

        payload = {
            'inprogress': add_strategies(inprogress),
            'completed': add_strategies(completed),
            'closed': add_strategies(closed),
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetStrategyView(APIView):
    def get(self, request, format=None):
        slug = request.GET.get("slug")
        strategy = Strategy.objects.filter(slug=slug)
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
        return Response({"message": "strategy not found!"}, status=status.HTTP_404_NOT_FOUND)