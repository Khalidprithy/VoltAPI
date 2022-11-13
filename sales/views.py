from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class CreateSaleView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup = request.GET.get('startup')
        salesModule = SalesModule.objects.get(startup=startup)
        sale = Sale.objects.create(
            TYPE_CHOICES = data.get("TYPE_CHOICES"),
            STATUS_CHOICES = data.get("STATUS_CHOICES"),
            SUCCESS_CHOICES = data.get("SUCCESS_CHOICES"),
            strategy = data.get("strategy"),
            salesTitle = data.get("salesTitle"),
            salesLeader = data.get("salesLeader"),
            type = data.get("type"),
            status = data.get("status"),
            description = data.get("description"),
            startDate = data.get("startDate"),
            endDate = data.get("endDate"),
            success = data.get("success")
        )
        sale.salesModule = salesModule
        return Response({"message": "done"})

class GetStrategyView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        salesModule = SalesModule.objects.get(startup=startup)
        your_sales = Sale.objects.filter(salesModule=salesModule)
        your_sales_data = SaleSerializer(your_sales, many=True).data
        payload = {
            'your_sales': your_sales_data
        }
        return Response(payload, status=status.HTTP_200_OK)