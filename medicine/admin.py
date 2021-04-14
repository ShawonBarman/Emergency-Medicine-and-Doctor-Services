from django.contrib import admin
from .models import *
# Register your models here.
class AddMedicine(admin.ModelAdmin):
    list_display = ('medicine_id','medicine_name','company_name','strength','pack_size','price_BDT','medicine_pic')

admin.site.register(Medicine,AddMedicine)

admin.site.register(Category)


class AddMedicineShop(admin.ModelAdmin):
    list_display = ('shop_id','shop_name','shop_email','shop_location')

admin.site.register(MedicineShop,AddMedicineShop)

class AddMedicineStoreShop(admin.ModelAdmin):
    list_display = ('shop_id','medicine_id')

admin.site.register(StoreMedicine,AddMedicineStoreShop)

class AddMedicineSupplier(admin.ModelAdmin):
    list_display = ('medicine_id','supplier_id','supplier_name','contact_number','address')

admin.site.register(MedicineSupplier,AddMedicineSupplier)

class AddEmployee(admin.ModelAdmin):
    list_display = ('shop_id','employee_id','employee_name','contact_number','address','profile_pic')

admin.site.register(Employee,AddEmployee)