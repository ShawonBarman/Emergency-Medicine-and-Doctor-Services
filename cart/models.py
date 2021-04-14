from django.db import models
from django.contrib.auth.models import User
from medicine.models import Medicine


# Create your models here.

class ShopCart(models.Model):
    medicines = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.medicines.name
