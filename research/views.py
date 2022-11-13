from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class CreateResearchView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup = request.GET.get('startup')
        researchModule = ResearchModule.objects.get(startup=startup)
        research = Research.objects.create(
            CATEGORY_CHOICES = data.get("CATEGORY_CHOICES"),
            strategy = data.get("strategy"),
            researchTitle = data.get("researchTitle"),
            category = data.get("category"),
            researchLeader = data.get("researchLeader"),
            researchTask = data.get("researchTask"),
            conclusion = data.get("conclusion"),
            researchArtifacts = data.get("researchArtifacts")
        )
        research.researchModule = researchModule
        return Response({"message": "done"})

class GetStrategyView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        researchModule = ResearchModule.objects.get(startup=startup)
        your_research = Research.objects.filter(researchModule=researchModule)
        your_research_data = ResearchSerializer(your_research, many=True).data
        payload = {
            'your_research': your_research_data
        }
        return Response(payload, status=status.HTTP_200_OK)