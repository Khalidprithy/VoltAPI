from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class CreateResearchTaskView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup_key = data.get('startup_key')
        researchModule = ResearchModule.objects.get(startup__key=startup_key)
        if len(data.get("marketing_key"))==10:
            marketing = Marketing.objects.get(marketing__key=data.get("marketing_key"))
            research = Research.objects.create(
                researchModule=researchModule,
                marketing = marketing,
                task = data.get("task"),
                category = data.get("category"),
                assigned_to = User.objects.get(username=data.get("assigned_to")),
                deadline = data.get("deadline"),
                volts = data.get("volts"),
            )

        research = Research.objects.create(
            researchModule=researchModule,
            task = data.get("task"),
            category = data.get("category"),
            assigned_to = User.objects.get(username=data.get("assigned_to")),
            deadline = data.get("deadline"),
            volts = data.get("volts"),
        )
        return Response({"message": "done"})

class GetResearchView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        researchModule = ResearchModule.objects.get(startup=startup)
        your_research = Research.objects.filter(researchModule=researchModule)
        your_research_data = ResearchSerializer(your_research, many=True).data
        payload = {
            'your_research': your_research_data
        }
        return Response(payload, status=status.HTTP_200_OK)