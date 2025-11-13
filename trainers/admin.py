from django.contrib import admin
from .models import Trainer

# Register your models here.

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'specialization', 'years_of_experience', 'is_active')
    list_filter = ('department', 'specialization', 'is_active', 'joined_date')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    ordering = ('last_name', 'first_name')
    list_per_page = 20
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Professional Details', {
            'fields': ('department', 'specialization', 'years_of_experience', 'joined_date')
        }),
        ('Additional Information', {
            'fields': ('bio', 'is_active'),
            'classes': ('collapse',)
        }),
    )
