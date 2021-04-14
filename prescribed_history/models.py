from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
# Create your models here.
class PrescribedHistory(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=8)
    date = models.CharField(max_length=10)
    discase = models.TextField()
    prescription = models.TextField()