from django.db import models

# Create your models here.

class Trainer(models.Model):
    """Model representing a trainer at NIE College"""
    
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('ME', 'Mechanical Engineering'),
        ('EC', 'Electronics & Communication'),
        ('CV', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('IS', 'Information Science'),
    ]
    
    SPECIALIZATION_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('ML', 'Machine Learning'),
        ('WEB', 'Web Development'),
        ('DB', 'Database Management'),
        ('NW', 'Networking'),
        ('OTHER', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    specialization = models.CharField(max_length=5, choices=SPECIALIZATION_CHOICES)
    years_of_experience = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_department_display()}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
