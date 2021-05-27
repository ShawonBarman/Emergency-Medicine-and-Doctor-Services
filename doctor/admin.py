from django.contrib import admin
from .models import *
# Register your models here.
class AddDoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id','name','user_name','email','contact_number','specialist','schedule','address','profile_pic')

admin.site.register(Doctor,AddDoctorAdmin)