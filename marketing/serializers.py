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


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"