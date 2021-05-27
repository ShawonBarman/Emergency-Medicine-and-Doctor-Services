from django.shortcuts import render
from .models import Doctor
# Create your views here.
doctor = Doctor.objects.all()
print(doctor[1].name)