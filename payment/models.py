import uuid
from datetime import datetime

import obj as obj
import order as order
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import F

from products.models import Pooja

Nakshatram = [
    ('ch', 'Chathayam')
]


class Order(models.Model):
    # auto generated
    orderID = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now=True)
    # added on save function
    issuer = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)

    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name='Name of Person',
        help_text='Please enter the person for whom the pooja is being booked',
    )
    nakshatram = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=Nakshatram,
        verbose_name='Select Nakshtram',
    )
    products = models.ManyToManyField(Pooja, through='OrderProduct')

    def __str__(self):
        return str(self.name)

    # intermediate model connecting products & order


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pooja = models.ForeignKey(Pooja, on_delete=models.PROTECT)

    price = models.PositiveIntegerField(null=True, blank=True, editable=False)
    date = models.DateTimeField(null=True, blank=True, verbose_name='Booking Date')
    qty = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Order Products"
        verbose_name = "Order Product"

    def __str__(self):
        return str(self.pooja.pooja + ' - ' + self.order.name)
