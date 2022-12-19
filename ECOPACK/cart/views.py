from django.shortcuts import render

from . import models

from products.models import Product

from users.models import CustomUser

from products.views import List_of_products

import json




def List_of_products_in_the_shopping_cart(request):

    user_shopping_cart = models.Product_in_cart.objects.filter(user_id=request.user.pk)[0]
    total_price_of_products = 0
    products_list_in_cart = []

    try:
        for products in user_shopping_cart.products['products']:

            product = Product.objects.filter(id=products['id'])[0] #сущность продукта
            total_price_of_products += int(products['quantity']) * float(product.price)
            product.price = product.price * int(products['quantity'])
            product.number_of_items_in_cart = int(products['quantity'])
            products_list_in_cart.append(product) #добавление в массив

        number_of_positions = len(user_shopping_cart.products['products'])

    except:
        number_of_positions = 0

    return render(request, 'shopping_cart.html', {'object_list': products_list_in_cart, 'sum': total_price_of_products,
                                                  'cart_num': number_of_positions, 'user': CustomUser.objects.get(id=request.user.id)})




def adding_products_to_cart(request, product_id):

    try:
        item = models.Product_in_cart.objects.filter(user_id=request.user.pk)[0]

        if item.user_id == request.user:

            for i in range(len(item.products['products'])):

                if item.products['products'][i]['id'] == product_id: #если есть продукт в корзине

                    item.products['products'][i]['quantity'] += 1
                    item.save()

                    return List_of_products(request)

            item.products['products'].append(json.loads('{"id":%s, "quantity": 1}' % (product_id))) #если нет продукта в корзине
            item.save()

            return List_of_products(request)

    except:

        data = json.loads('{"products": [{"id":%s, "quantity": 1}]}' % (product_id))
        new_shopping_cart = models.Product_in_cart.objects.create(user_id=request.user, products=data)

    return List_of_products(request)




def product_interaction(request, pk, choices):

    user_shopping_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)

    if choices == 1:

        for i in range(len(user_shopping_cart.products['products'])):

            if user_shopping_cart.products['products'][i]['id'] == pk:

                user_shopping_cart.products['products'][i]['quantity'] += 1
                user_shopping_cart.save()

        return List_of_products_in_the_shopping_cart(request)

    elif choices == 2:

        for i in range(len(user_shopping_cart.products['products'])):

            if user_shopping_cart.products['products'][i]['id'] == pk:

                user_shopping_cart.products['products'][i]['quantity'] -= 1

                if user_shopping_cart.products['products'][i]['quantity'] <= 0:

                    user_shopping_cart.products['products'].pop(i)

            user_shopping_cart.save()

        return List_of_products_in_the_shopping_cart(request)

    elif choices == 3:

        for i in range(len(user_shopping_cart.products['products'])):

            if user_shopping_cart.products['products'][i]['id'] == pk:

                user_shopping_cart.products['products'].pop(i)
                user_shopping_cart.save()

                return List_of_products_in_the_shopping_cart(request)

        return List_of_products_in_the_shopping_cart(request)

    else:

        return List_of_products_in_the_shopping_cart(request)

