from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Dog(BaseModel):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)

    class Meta:
        app_label = 'myapp'

class Vet(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'myapp'

class HealthRecord(BaseModel):
    summary = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)

    class Meta:
        app_label = 'myapp'
