from rest_framework import serializers
from .models import *




class MarketingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingModule
        fields = "__all__"


class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = "__all__"


class MarketingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingTask
        fields = "__all__"
