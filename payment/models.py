import uuid
from datetime import datetime

import obj as obj
import order as order
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import F

from products.models import Pooja


class Order(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    orderID = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    issuer = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField()
    products = models.ManyToManyField(Pooja, through='OrderProduct')

    def __str__(self):
        return str(self.name)


class OrderProduct(models.Model):
    pooja = models.ForeignKey(Pooja, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total = models.IntegerField()

    class Meta:
        verbose_name_plural = "Order Products"
        verbose_name = "Order Product"

    def __str__(self):
        return str(self.pooja.pooja + ' - ' + self.order.name)

    def save_model(self, request, obj, form, change):
        obj.lastEditor = request.user
        obj.lastEditTime = datetime.now()
        super().save_model(request, obj, form, change)
        for product in OrderProduct.objects.filter(order=order):
            cost = cost + product.price * product.qty
            obj.total = cost

    class Competition(models.Model):
        lastEditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
        lastEditTime = models.DateTimeField(null=True, blank=True)





