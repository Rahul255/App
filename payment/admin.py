from django.contrib import admin

# Register your models here.
from payment.inlines import OPInline
from payment.models import Order, OrderProduct, SumValue


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'orderID', 'amount')
    inlines = (OPInline,)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('pooja', 'qty', 'price', 'date', 'objects')


@admin.register(SumValue)
class SumValueAdmin(admin.ModelAdmin):
    pass
