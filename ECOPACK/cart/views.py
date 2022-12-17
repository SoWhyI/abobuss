from django.shortcuts import render

from . import models

import json

from products.models import Product

from products.views import List_of_products

from users.models import CustomUser


def List_of_products_in_the_shopping_cart(request):
    user_shopping_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    total_price_of_products = 0
    products_list_in_cart = []

    try:
        for products in user_shopping_cart.products['products']:
            product = Product.objects.get(id=products['id'])
            total_price_of_products += int(products['quan']) * float(product.price)
            product.price = product.price * int(products['quan'])
            product.quantity_in_cart = int(products['quan'])
            products_list_in_cart.append(product)
        number_of_positions = len(user_shopping_cart.products['products'])
    except:
        number_of_positions = 0

    return render(request, 'shopping_cart.html', {'object_list': products_list_in_cart, 'sum': total_price_of_products,
                                                  'cart_num': number_of_positions,
                                                  'user': CustomUser.objects.get(id=request.user.id)})


def cart_add(request, product_id):
    try:
        object = models.Product_in_cart.objects.get(user_id=request.user.pk)
        if object.user_id == request.user:
            for i in range(len(object.products['products'])):
                if object.products['products'][i]['id'] == product_id:
                    object.products['products'][i]['quan'] += 1
                    object.save()
                    return List_of_products(request)

            object.products['products'].append(json.loads('{"id":%s, "quan": 1}' % (product_id)))
            object.save()
            return List_of_products(request)
    except:
        data = json.loads('{"products": [{"id":%s, "quan": 1}]}' % (product_id))
        new_cart = models.Product_in_cart.objects.create(user_id=request.user, products=data)
    return List_of_products(request)


def product_interaction(request, pk, choices):
    user_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    if choices == 1:
        for i in range(len(user_cart.products['products'])):
            if user_cart.products['products'][i]['id'] == pk:
                user_cart.products['products'][i]['quan'] += 1
                user_cart.save()
        return List_of_products_in_the_shopping_cart(request)
    elif choices == 2:
        for i in range(len(user_cart.products['products'])):
            if user_cart.products['products'][i]['id'] == pk:
                user_cart.products['products'][i]['quan'] -= 1
                if user_cart.products['products'][i]['quan'] <= 0:
                    user_cart.products['products'].pop(i)
            user_cart.save()
        return List_of_products_in_the_shopping_cart(request)
    elif choices == 3:
        for i in range(len(user_cart.products['products'])):
            if user_cart.products['products'][i]['id'] == pk:
                user_cart.products['products'].pop(i)
                user_cart.save()
                return List_of_products_in_the_shopping_cart(request)
        return List_of_products_in_the_shopping_cart(request)
    else:
        return List_of_products_in_the_shopping_cart(request)