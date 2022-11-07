from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from .models import *
from .serializers import *


# Create your views here.
class StartupViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = StartupSerializer
    queryset = Startup.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        baseModel = Startup.objects.get(profile=profile)
        if request.method == 'GET':
            serializer = StartupSerializer(baseModel)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = StartupSerializer(baseModel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class PublicStartupViewSet(ReadOnlyModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = PublicStartupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'users__first_name', 'users__last_name']

    def get_serializer_context(self):
        return {'request': self.request}


class ProfileViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get', 'put'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        if request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class PublicProfileViewSet(ModelViewSet):
    serializer_class = PublicProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'user__last_name']

    def get_serializer_context(self):
        return {'request': self.request}
