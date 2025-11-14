from rest_framework import serializers
from .models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    """Serializer for the Trainer model"""
    
    full_name = serializers.SerializerMethodField()
    department_display = serializers.CharField(source='get_department_display', read_only=True)
    specialization_display = serializers.CharField(source='get_specialization_display', read_only=True)
    
    class Meta:
        model = Trainer
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'phone',
            'department',
            'department_display',
            'specialization',
            'specialization_display',
            'years_of_experience',
            'bio',
            'is_active',
            'joined_date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_full_name(self, obj):
        return obj.get_full_name()


class TrainerListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for trainer list view"""
    
    full_name = serializers.SerializerMethodField()
    department_display = serializers.CharField(source='get_department_display', read_only=True)
    specialization_display = serializers.CharField(source='get_specialization_display', read_only=True)
    
    class Meta:
        model = Trainer
        fields = [
            'id',
            'full_name',
            'email',
            'department',
            'department_display',
            'specialization',
            'specialization_display',
            'years_of_experience',
        ]
    
    def get_full_name(self, obj):
        return obj.get_full_name()
