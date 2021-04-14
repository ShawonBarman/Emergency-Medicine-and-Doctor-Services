from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
import datetime
# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    patientName=models.CharField(max_length=40,null=True)
    phone = models.CharField(max_length=14, default="")
    address = models.TextField(default='')
    applyAppointmentDate = models.DateField(default=datetime.datetime.today)
    appointmentDate = models.DateField(auto_now=True)
    description=models.TextField(max_length=500,default='')
    status=models.BooleanField(default=False)
    def placeAppointment(self):
        self.save()

    @staticmethod
    def getUserByID(userId):
        return Appointment.objects.filter(user=userId)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=300)

class ProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, null=True)
    contact_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    about = models.TextField(null=True)
    profile_pic = models.ImageField(default='default.png',upload_to='profile_pictures')