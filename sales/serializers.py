from rest_framework import serializers
from .models import *



class SalesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesModule
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class SalesTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTask
        fields = "__all__"
