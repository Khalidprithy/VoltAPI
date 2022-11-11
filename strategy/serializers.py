from rest_framework import serializers
from .models import *




class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'strategy', 'category', 'approxStartDate', 'strategyLeader', 'Customer', 'features',
                  'description', 'success']


class StrategyModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyModule
        fields = ['id', 'customer', 'problemArea', 'uses']

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
"""
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
        return instance"""
