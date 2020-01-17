from django.contrib import admin

# Register your models here.
from payment.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'orderID', 'amount')


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('pooja', 'qty', 'price', 'date', 'order')
