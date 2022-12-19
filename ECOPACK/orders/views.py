from django.shortcuts import render
from . import models
from products.models import Product
from cart.models import Product_in_cart
from users.models import CustomUser

import json


def List_of_user_orders(request):

    user_orders = models.Order.objects.filter(user_id=request.user.pk)
    total_price_of_products = []

    for i in range(len(user_orders)):

        order = user_orders[i]
        sum_of_prices = 0
        products_list = []

        for products in order.product_list['products']: #перевод продуктов из json в сущности

            product = Product.objects.get(id=products['id'])
            sum_of_prices += int(products['quantity']) * float(product.price)
            product.price = product.price * int(products['quantity'])
            product.quantity_in_cart = int(products['quantity'])
            products_list.append(product)
            user_orders[i].product_list = products_list
            total_price_of_products.append(sum_of_prices)

    return render(request, 'user_orders_detail.html', {'object_list':  reversed(user_orders), 'sum': total_price_of_products, 'user': CustomUser.objects.get(id=request.user.id)})

def Add_the_order_to_the_users_order_list(request):

    user_cart = Product_in_cart.objects.get(user_id=request.user.pk)

    if len(user_cart.products['products']) != 0:

        new_order = models.Order.objects.create(user_id=request.user, product_list=user_cart.products)
        user_cart.products = json.loads('{"products": []}')
        user_cart.save()

    else:
        pass

    return List_of_user_orders(request)
