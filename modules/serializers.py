from rest_framework import serializers
from modules.models import BasicModel, StrategyModel, Up, Segment, Influencer, Strategy, ResearchModel, Research, \
    Marketing, MarketingModel, MarketingTask, SalesModel, Sale, SalesTask, Partner, Profile
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


class BasicModelSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = BasicModel
        fields = ['id', 'name', 'idea', 'problemArea', 'currentPlayers', 'difference', 'customer', 'revenueQuestion',
                  'revenueAnswer', 'stage', 'created_at', 'points', 'profile']


class PublicBasicModelSerializer(serializers.ModelSerializer):
    profile = PublicProfileSerializer(many=True, read_only=True)

    class Meta:
        model = BasicModel
        fields = ['id', 'name', 'created_at', 'points', 'profile']


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


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'strategy', 'category', 'approxStartDate', 'strategyLeader', 'Customer', 'features',
                  'description', 'success']


class StrategyModelSerializer(serializers.ModelSerializer):
    ups = UpSerializer(many=True, read_only=False)
    segments = SegmentSerializer(many=True, read_only=False)
    partners = PartnerSerializer(many=True, read_only=False)
    influencers = InfluencerSerializer(many=True, read_only=True)
    strategies = StrategySerializer(many=True, read_only=True)

    class Meta:
        model = StrategyModel
        fields = ['id', 'customer', 'problemArea', 'uses', 'ups', 'segments', 'partners', 'influencers', 'strategies']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     profile = Profile.objects.get(user=user)
    #     basicModel = BasicModel.objects.get(profile=profile)
    #     ups_data = validated_data.pop('ups')
    #     segments_data = validated_data.pop('segments')
    #     partners_data = validated_data.pop('partners')
    #     if StrategyModel.objects.filter(basicModel=basicModel).exists():
    #         strategyModel = StrategyModel.objects.get(basicModel=basicModel)
    #         strategyModel.customer = validated_data['customer']
    #         strategyModel.problemArea = validated_data['problemArea']
    #         strategyModel.uses = validated_data['uses']
    #         strategyModel.save()
    #     else:
    #         strategyModel = StrategyModel.objects.create(basicModel=basicModel, customer=validated_data['customer'],
    #                                                      problemArea=validated_data['problemArea'],
    #                                                      uses=validated_data['uses'])
    #     if ups_data:
    #         for up in ups_data:
    #             Up.objects.create(strategyModel=strategyModel, **up)
    #     if segments_data:
    #         for segment in segments_data:
    #             Segment.objects.create(strategyModel=strategyModel, **segment)
    #     if partners_data:
    #         for partner in partners_data:
    #             Partner.objects.create(strategyModel=strategyModel, **partner)
    #     return strategyModel

    def update(self, instance, validated_data):
        ups_data = validated_data.pop('ups')
        segments_data = validated_data.pop('segments')
        partners_data = validated_data.pop('partners')
        instance.customer = validated_data.get('customer', instance.customer)
        instance.problemArea = validated_data.get('problemArea', instance.problemArea)
        instance.uses = validated_data.get('uses', instance.uses)
        instance.save()
        if ups_data:
            for up in ups_data:
                if 'id' in up:
                    up_obj = Up.objects.get(id=up['id'])
                    up_obj.ups = up['ups']
                    up_obj.save()
                else:
                    Up.objects.create(strategyModel=instance, **up)
        if segments_data:
            for segment in segments_data:
                if 'id' in segment:
                    segment_obj = Segment.objects.get(id=segment['id'])
                    segment_obj.segments = segment['segments']
                    segment_obj.save()
                else:
                    Segment.objects.create(strategyModel=instance, **segment)
        if partners_data:
            for partner in partners_data:
                if 'id' in partner:
                    partner_obj = Partner.objects.get(id=partner['id'])
                    partner_obj.partners = partner['partners']
                    partner_obj.save()
                else:
                    Partner.objects.create(strategyModel=instance, **partner)
        return instance


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
        model = ResearchModel
        fields = ['id', 'additionalArticles', 'researches']
        read_only_fields = ['id', 'researches']


class MarketingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingModel
        fields = "__all__"


class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = "__all__"


class MarketingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingTask
        fields = "__all__"


class SalesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class SalesTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTask
        fields = "__all__"
