from django.shortcuts import render , redirect
from django.views import  View
from medicine.models import Medicine


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('addCart').keys())
        products = Medicine.get_products_by_id(ids)
        return render(request , 'medicine_services.html' , {'products' : products} )