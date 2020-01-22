from django.contrib import admin

# Register your models here.
from payment.inlines import OPInline
from payment.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'orderID', 'issuer')
    list_filter = ('issuer', 'products')
    filter_horizontal = ('products',)
    inlines = (OPInline,)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.price = instance.pooja.price * instance.qty
            instance.save()
        formset.save_m2m()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.issuer = request.user
        super().save_model(request, obj, form, change)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('pooja', 'qty', 'price', 'date')
