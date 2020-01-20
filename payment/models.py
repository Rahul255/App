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
    issuer = models.CharField(max_length=150, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField()
    products = models.ManyToManyField(Pooja, through='OrderProduct')
    total = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    lastEditTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save_model(self, request, obj, form, change):
        obj.total = request.user
        obj.lastEditTime = datetime.now()
        for product in OrderProduct.objects.filter(order=Order):
            cost = cost + product.price * product.qty
            obj.total = cost
        super().save_model(request, obj, form, change)


class OrderProduct(models.Model):
    pooja = models.ForeignKey(Pooja, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Order Products"
        verbose_name = "Order Product"

    def __str__(self):
        return str(self.pooja.pooja + ' - ' + self.order.name)
