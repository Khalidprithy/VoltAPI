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

class GetResearchModuleView(APIView):
    def get(self, request, format=None):
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        drafts = Research.objects.filter(researchModule__startup=startup, status='D')
        contents = Research.objects.filter(researchModule__startup=startup, status='C')
        tasks = Research.objects.filter(researchModule__startup=startup, status='T')

        payload = {
            'drafts': PublicResearchSerializer(drafts, many=True).data,
            'contents': ContentSerializer(contents, many=True).data,
            'tasks': PublicResearchSerializer(tasks, many=True).data
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetResearchTaskView(APIView):
    def get(self, request, format=None):
        research_key = request.GET.get('research_key')
        payload = {
            'research': PublicResearchSerializer(Research.objects.get(key=research_key)).data
        }
        return Response(payload, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        research_key = request.GET.get('research_key')
        data = request.data
        research = Research.objects.get(key=research_key)
        research.video = data.get('video')
        research.img = data.get('img')
        research.conclusion = data.get('conclusion')

        research.save(update_fields=['img', 'video', 'conclusion'])

class GetResearchContentView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        researchModule = ResearchModule.objects.get(startup=startup)
        your_research = Research.objects.filter(researchModule=researchModule)
        your_research_data = ResearchSerializer(your_research, many=True).data
        payload = {
            'your_research': your_research_data
        }
        return Response(payload, status=status.HTTP_200_OK)
    
class GetResearchDraftView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        researchModule = ResearchModule.objects.get(startup=startup)
        your_research = Research.objects.filter(researchModule=researchModule)
        your_research_data = ResearchSerializer(your_research, many=True).data
        payload = {
            'your_research': your_research_data
        }
        return Response(payload, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        pass