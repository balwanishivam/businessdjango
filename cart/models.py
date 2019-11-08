from django.db import models
from user.models import *
from business.models import *

class Customer(details):
    email=models.CharField(max_length=200)

class sale(models.Model):
    total_items=models.PositiveIntegerField()
    total_amt=models.DecimalField(max_digits=15 , decimal_places=2)

class item_purchased(models.Model):
    customer_id=models.ForeignKey(Customer ,on_delete=models.CASCADE)
    item_purchased_id=models.ForeignKey(Stock , on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    date_of_purchase=models.DateField(auto_now_add=True)


# Create your models here.
