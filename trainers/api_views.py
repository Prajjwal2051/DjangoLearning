from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Trainer
from .serializers import TrainerSerializer, TrainerListSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Trainers
    
    Provides CRUD operations for trainers with search and filtering
    """
    queryset = Trainer.objects.filter(is_active=True)
    serializer_class = TrainerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['last_name', 'first_name', 'years_of_experience', 'joined_date']
    ordering = ['last_name', 'first_name']
    
    def get_serializer_class(self):
        """Use lightweight serializer for list view"""
        if self.action == 'list':
            return TrainerListSerializer
        return TrainerSerializer
    
    def get_queryset(self):
        """
        Filter trainers by department and specialization
        """
        queryset = super().get_queryset()
        
        # Filter by department
        department = self.request.query_params.get('department', None)
        if department:
            queryset = queryset.filter(department=department)
        
        # Filter by specialization
        specialization = self.request.query_params.get('specialization', None)
        if specialization:
            queryset = queryset.filter(specialization=specialization)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def choices(self, request):
        """
        Get department and specialization choices
        """
        return Response({
            'departments': [
                {'value': choice[0], 'label': choice[1]}
                for choice in Trainer.DEPARTMENT_CHOICES
            ],
            'specializations': [
                {'value': choice[0], 'label': choice[1]}
                for choice in Trainer.SPECIALIZATION_CHOICES
            ]
        })
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Get statistics about trainers
        """
        queryset = self.get_queryset()
        
        return Response({
            'total_trainers': queryset.count(),
            'by_department': {
                dept[0]: queryset.filter(department=dept[0]).count()
                for dept in Trainer.DEPARTMENT_CHOICES
            },
            'by_specialization': {
                spec[0]: queryset.filter(specialization=spec[0]).count()
                for spec in Trainer.SPECIALIZATION_CHOICES
            }
        })
