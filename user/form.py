from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import *

'''
from .models import Contact
class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ['name',
                  'email',
                  'message',
                  ]
'''

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]

# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#
#     class Meta:
#         model = Contact
#         fields = ['Name',
#                   'Email',
#                   'Message',
#                   ]

class UserContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name',
                  'email',
                  'message',
                 ]

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label="username :", required=False)
    first_name = forms.CharField(max_length=30, label="First Name :", required=False)
    last_name = forms.CharField(max_length=30, label="Last Name :", required=False)
    email = forms.EmailField(label="Email Address :", required=False)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

class ProfileUpdateForm(forms.ModelForm):
    gender = forms.CharField(label="Gender :", max_length=6,required=False)
    contact_number = forms.IntegerField(label="Contact Number :",required=False)
    address = forms.CharField(label="Address :", max_length=100,required=False)
    about = forms.CharField(label="About yourself :", max_length=300, required=False)
    profile_pic = forms.ImageField(label="Profile picture :", required=False)
    class Meta:
        model = ProfileDetails
        fields = (
            'gender',
            'contact_number',
            'address',
            'about',
            'profile_pic',
        )