from rest_framework import serializers
from .models import *


class ProductModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModule
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class PublicProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("productModule", "desc", "phase", "keyword", "completed")



class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class PublicFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        exclude = ("desc", "product", "completed")

class TimelineSerializer(serializers.ModelSErializer):
    class Meta:
        model = Timeline
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

