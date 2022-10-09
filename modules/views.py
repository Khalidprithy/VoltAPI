from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from modules.models import BasicModel, User, StrategyModel, ResearchModel, Profile, Research
from modules.serializers import BasicModelSerializer, PublicBasicModelSerializer, ProfileSerializer, \
    StrategyModelSerializer, ResearchModelSerializer, PublicProfileSerializer, ResearchSerializer


# Create your views here.
class BasicModelViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = BasicModelSerializer
    queryset = BasicModel.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        baseModel = BasicModel.objects.get(profile=profile)
        if request.method == 'GET':
            serializer = BasicModelSerializer(baseModel)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = BasicModelSerializer(baseModel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class PublicBasicModelViewSet(ReadOnlyModelViewSet):
    queryset = BasicModel.objects.all()
    serializer_class = PublicBasicModelSerializer
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


class StrategyModelViewSet(UpdateModelMixin, GenericViewSet):
    serializer_class = StrategyModelSerializer
    queryset = StrategyModel.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        basicModel = BasicModel.objects.get(profile=profile)
        try:
            strategyModel = StrategyModel.objects.get(basicModel=basicModel)
        except StrategyModel.DoesNotExist:
            strategyModel = StrategyModel.objects.create(basicModel=basicModel)
        if request.method == 'GET':
            serializer = StrategyModelSerializer(strategyModel)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = StrategyModelSerializer(strategyModel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class ResearchModelViewSet(ModelViewSet):
    serializer_class = ResearchModelSerializer
    queryset = ResearchModel.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def me(self, request):
        profile = Profile.objects.get(user=request.user)
        basicModel = BasicModel.objects.get(profile=profile)
        try:
            researchModel = ResearchModel.objects.get(basicModel=basicModel)
        except ResearchModel.DoesNotExist:
            researchModel = ResearchModel.objects.create(basicModel=basicModel)
        if request.method == 'GET':
            serializer = ResearchModelSerializer(researchModel)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ResearchModelSerializer(researchModel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class ResearchViewSet(UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ResearchSerializer
    queryset = Research.objects.all()

