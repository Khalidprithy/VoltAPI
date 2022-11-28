from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserCreatSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreatSerializer):
    class Meta(BaseUserCreatSerializer.Meta):
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'user', 'phone_number', 'founder', 'college', 'course',
                  'yearOfGraduation', 'dob', 'gender', 'founder', 'role', 'joined_on', 'image']
        depth = 1


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'gender', 'founder', 'role', 'joined_on', 'image']


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = "__all__"


class PublicStartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ['id', 'name', 'created_at', 'points', 'vision', 'founded', 'website', 'key', 'logo']

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'

class UpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Up
        fields = ['id', 'ups', 'strategyModel']
        read_only_fields = ['strategyModel']


class SegmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Segment
        fields = ['id', 'segments', 'strategyModel']
        read_only_fields = ['strategyModel']


class PartnerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Partner
        fields = ['id', 'partners', 'strategyModel']
        read_only_fields = ['strategyModel']


class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = ['id', 'influencers', 'how']


