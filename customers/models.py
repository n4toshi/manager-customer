from django.db import models
from django.utils import timezone
from managers.models import Manager


class Customer(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='manager')
    customer_name = models.CharField(max_length=25) 
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    photo = models.FileField(upload_to='photos', blank=True, null=True)
    debt = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)
    payments = models.IntegerField(default=0)
    cumulative_purchases = models.IntegerField(default=0)
    cumulative_payments = models.IntegerField(default=0)

    def __str__(self):
        return self.customer_name