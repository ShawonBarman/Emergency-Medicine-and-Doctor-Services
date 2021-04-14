from django.contrib import admin
from .models import *

class AddUserProfileDetails(admin.ModelAdmin):
    list_display = ('user_id','gender', 'contact_number', 'address', 'about', 'profile_pic')

admin.site.register(ProfileDetails,AddUserProfileDetails)