from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Trainer

# Create your views here.

def trainer_list(request):
    """View to list all trainers with search functionality"""
    query = request.GET.get('q', '')
    department = request.GET.get('department', '')
    specialization = request.GET.get('specialization', '')
    
    trainers = Trainer.objects.filter(is_active=True)
    
    # Search by name or email
    if query:
        trainers = trainers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    
    # Filter by department
    if department:
        trainers = trainers.filter(department=department)
    
    # Filter by specialization
    if specialization:
        trainers = trainers.filter(specialization=specialization)
    
    context = {
        'trainers': trainers,
        'query': query,
        'department': department,
        'specialization': specialization,
        'departments': Trainer.DEPARTMENT_CHOICES,
        'specializations': Trainer.SPECIALIZATION_CHOICES,
    }
    
    return render(request, 'trainers/trainer_list.html', context)


def trainer_detail(request, pk):
    """View to display details of a specific trainer"""
    trainer = get_object_or_404(Trainer, pk=pk, is_active=True)
    
    context = {
        'trainer': trainer,
    }
    
    return render(request, 'trainers/trainer_detail.html', context)
