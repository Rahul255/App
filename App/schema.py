from datetime import timedelta

import graphene

from App.local_settings import GST_RATE
from payment.models import Order, OrderProduct
from products.models import Pooja


class PoojaObj(graphene.ObjectType):
    name = graphene.String()
    price = graphene.Int()
    priceWithGST = graphene.Float()

    def resolve_name(self, info):
        if "pooja" not in self.name.lower():
            return self.name + ' pooja'
        return self.name

    def resolve_priceWithGST(self, info):
        return round(self.price + self.price * GST_RATE, 2)


class OrderProductObj(graphene.ObjectType):
    pooja = graphene.String()
    qty = graphene.Int()
    price = graphene.Int()
    date = graphene.String()

    def resolve_pooja(self, info):
        return self.pooja.name

    def resolve_price(self, info):
        if self.price:
            return self.price
        return 0


class OrderObj(graphene.ObjectType):
    orderID = graphene.String()
    total = graphene.Int()
    totalWithGST = graphene.Int()
    products = graphene.List(OrderProductObj)

    def resolve_products(self, info):
        return OrderProduct.objects.filter(order=self)

    def resolve_total(self, info):
        products = OrderProduct.objects.filter(order=self)
        total = 0
        for p in products:
            if p.price:
                total = total + p.price
        return total

    def resolve_totalWithGST(self, info):
        products = OrderProduct.objects.filter(order=self)
        total = 0
        for p in products:
            if p.price:
                total = total + p.price
        return total + total * GST_RATE


class Query(graphene.ObjectType):
    listPoojas = graphene.List(PoojaObj)
    listOrders = graphene.List(
        OrderObj,
        date=graphene.Date(required=False),
        pooja=graphene.String()
    )

    def resolve_listPoojas(self, info, **kwargs):
        return Pooja.objects.all()

    def resolve_listOrders(self, info, **kwargs):
        date = kwargs.get('date')
        pooja = kwargs.get('pooja')
        list = Order.objects.all()
        if date:
            list = list.filter(timestamp__gte=date, timestamp__lt=date + timedelta(days=1))
        return list


schema = graphene.Schema(query=Query)