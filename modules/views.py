from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from modules.models import BasicModel
from modules.serializers import BasicModelSerializer, BasicModelSearchSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def basicModel(request, pk):
    basicModel = get_object_or_404(BasicModel, pk=pk)
    serializer = BasicModelSerializer(basicModel)
    return Response(serializer.data)


@api_view(['GET'])
def basicModelSearch_list(request):
    queryset = BasicModel.objects.all()
    serializer = BasicModelSearchSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def basicModelSearch_detail(request, pk):
    basicModel = get_object_or_404(BasicModel, pk=pk)
    serializer = BasicModelSearchSerializer(basicModel)
    return Response(serializer.data)
