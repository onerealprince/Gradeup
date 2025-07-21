from rest_framework import serializers
from .models import StudyEvent

class StudyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyEvent
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
