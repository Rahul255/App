from django.contrib import admin

from payment.models import OrderProduct


class OPInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
