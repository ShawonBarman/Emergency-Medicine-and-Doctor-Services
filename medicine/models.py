from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def category():
        return Category.objects.all()

class Medicine(models.Model):
    medicine_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    medicine_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    strength = models.CharField(max_length=20, blank=True)
    pack_size = models.CharField(max_length=30, blank=True)
    price_BDT = models.FloatField()
    medicine_pic = models.ImageField(default='default.png', upload_to='medicine_picture')

    @staticmethod
    def get_medicines_by_id(ids):
        print(ids)
        return Medicine.objects.filter(medicine_id__in=ids)

    @staticmethod
    def get_product_by_id(category_id):
        if category_id:
            return Medicine.objects.filter(category_id=category_id)
        else:
            Medicine.objects.all()

    def __str__(self):
        return self.medicine_name

class MedicineShop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.TextField()
    shop_email = models.TextField()
    shop_location = models.TextField()

class StoreMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, null=True, on_delete=models.SET_NULL)
    shop = models.ForeignKey(MedicineShop, null=True, on_delete=models.SET_NULL)

class MedicineSupplier(models.Model):
    medicine = models.ForeignKey(Medicine,null=True,on_delete=models.SET_NULL)
    medicineShop = models.ForeignKey(MedicineShop,null=True,on_delete=models.SET_NULL)
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.TextField()
    contact_number = models.IntegerField()
    address = models.TextField()

class Employee(models.Model):
    shop = models.ForeignKey(MedicineShop, null=True, on_delete=models.SET_NULL)
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.TextField()
    contact_number = models.IntegerField()
    address = models.TextField()
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pictures')