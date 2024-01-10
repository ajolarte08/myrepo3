from django.shortcuts import render
from django.http import JsonResponse
from .models import Dog, Vet, HealthRecord

def get_dogs(request):
    dogs = Dog.objects.all().values()
    return JsonResponse({'dogs': list(dogs)})

def get_health_records(request):
    records = HealthRecord.objects.all().values()
    return JsonResponse({'health_records': list(records)})

def get_vets(request):
    vets = Vet.objects.all().values()
    return JsonResponse({'vets': list(vets)})

