from django.db import models
from medicine.models import Medicine
from django.contrib.auth.models import User
import datetime
# Create your models here.
class OrderDetails(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine,null=True,on_delete=models.CASCADE)
    order_date = models.CharField(max_length=10)
    delivery_date = models.CharField(max_length=10)

class Order(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine,null=True,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True)
    price = models.FloatField(null=True)
    phone = models.CharField(max_length=14, default="")
    address = models.TextField(default='')
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    @staticmethod
    def getUserByID(userId):
        return Order.objects.filter(user=userId)