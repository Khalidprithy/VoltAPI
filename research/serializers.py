from rest_framework import serializers
from .models import *



class ResearchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Research
        fields = ['id', 'strategy', 'researchTitle', 'category', 'researchLeader', 'researchTask',
                  'conclusion',
                  'researchArtifacts']
        read_only_fields = ['strategy', 'researchTitle', 'category', 'id']

    strategy = serializers.StringRelatedField(many=False, read_only=True)


class ResearchModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ResearchModule
        fields = ['id', 'additionalArticles', 'researches']
        read_only_fields = ['id', 'researches']
