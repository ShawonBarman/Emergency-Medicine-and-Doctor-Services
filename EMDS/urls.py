"""EMDS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.homepage, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='user_login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_logout.html'),name='logout'),
    path('register/', user_views.registration, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profileUpdate/', user_views.profile_update, name='profileUpdate'),
    path('aboutus/', user_views.aboutpage, name='aboutus'),
    path('contactus/', user_views.contactus, name='contactus'),
    path('contactussuccess/', user_views.contactusSuccess, name='contactusSuccess'),
    path('doctorservices/', user_views.doctorServices, name='doctorservices'),
    path('medicinestore/', user_views.medicinestore, name='medicineservices'),
    path('cart/', user_views.cart, name='cart'),
    path('check-out/',user_views.check_out,name='check-out'),
    path('order/',user_views.orderPage,name='order'),
    path('appointmentCheck-out/',user_views.appointmentCheckout,name='appointmentCheck-out'),
    path('appointmentDetails/',user_views.appointmentPage,name='appointmentDetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
