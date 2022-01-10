from rest_framework import serializers
from .models import Project, Risk


class RiskSerializer(serializers.ModelSerializer):
    background = serializers.CharField(source='get_background_display')
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')

    class Meta:
        model = Risk
        fields = ['name', 'background', 'user_assigned', 'priority', 'probability_percentage']


class ProjectSerializer(serializers.ModelSerializer):
    risks = RiskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'users_assigned', 'risks']
        depth = 1


class DetailedRiskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(many=False)
    background = serializers.CharField(source='get_background_display')
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')

    class Meta:
        model = Risk
        fields = ['name', 'project', 'background', 'user_assigned', 'priority', 'probability_percentage']





