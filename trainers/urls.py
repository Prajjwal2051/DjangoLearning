from django.urls import path
from . import views

app_name = 'trainers'

urlpatterns = [
    path('', views.trainer_list, name='trainer_list'),
    path('<int:pk>/', views.trainer_detail, name='trainer_detail'),
]
