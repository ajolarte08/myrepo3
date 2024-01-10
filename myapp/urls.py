from django.urls import path
from .views import get_dogs, get_health_records, get_vets

urlpatterns = [
    path('dogs/', get_dogs, name='get_dogs'),
    path('health_records/', get_health_records, name='get_health_records'),
    path('vets/', get_vets, name='get_vets'),
]
