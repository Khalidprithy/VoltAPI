from rest_framework import serializers
from modules.models import BasicModel, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicModel
        fields = "__all__"


class BasicModelSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicModel
        fields = ['id', 'name', 'created_at', 'points', 'users']

    users = serializers.StringRelatedField(many=True)
