from django.db import models
# Create your models here.
class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    contact_number = models.IntegerField()
    specialist = models.CharField(max_length=50)
    schedule = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pictures')

    @staticmethod
    def get_doctor_by_id(id):
        print(id)
        return Doctor.objects.filter(doctor_id=id)
