from django.db import models
from django.contrib.auth.models import User
from order.models import OrderDetails
# Create your models here.
class PaymentDetails(models.Model):
    invoice_number = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderDetails, null=True, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()
    payment_date = models.CharField(max_length=10)