from rest_framework import serializers
from .models import *


class PublicResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        exclude = ("researchModule", "marketing", "volts")

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = "__all__"


class ResearchModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ResearchModule
        fields = ['id', 'additionalArticles', 'researches']
        read_only_fields = ['id', 'researches']
