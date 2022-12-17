from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('detail/', views.List_of_products_in_the_shopping_cart, name='shopping_cart'),
    path('choice/full_delete/<int:pk>/<int:choices>', views.product_interaction, name='product_full_delete'),
    path('choice/add/<int:pk>/<int:choices>', views.product_interaction, name='product_add'),
    path('choice/remove/<int:pk>/<int:choices>', views.product_interaction, name='product_remove'),
]