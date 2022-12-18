from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from cart.models import Product_in_cart

from . import forms
from . import models

class ProductRemoveView(LoginRequiredMixin, DeleteView):

    model = models.Product
    template_name = 'product_remove.html'
    success_url = reverse_lazy('list_of_products')
    login_url = 'login'



class ProductChangesView(LoginRequiredMixin, UpdateView):

    model = models.Product
    fields = ['name', 'price', 'size', 'layer_field', 'category', 'picture']
    template_name = 'product_changes.html'
    login_url = 'login'

def List_of_products(request):

    products = models.Product.objects.all()

    try:

        number_of_positions = len((Product_in_cart.objects.get(user_id=request.user.pk)).products['products'])

    except:

        number_of_positions = 0

    categories = []

    for i in range(len(products)):

        if products[i].category in categories:

            pass

        else:

            categories.append(products[i].category)

    return render(request, 'list_of_products.html', {'object_list': products,  'cart_num': number_of_positions, 'categories': categories})


def image_request(request):

    if request.method == 'POST':

        form = forms.UserImage(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            img_object = form.instance

            return render(request, 'product_creation.html', {'form': form, 'img_obj': img_object})

    else:

        form = forms.UserImage()

    return render(request, 'product_creation.html', {'form': form})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
