from django.urls import path
from . import views


urlpatterns = [
    path('user_orders_detail/', views.List_of_user_orders, name='user_orders_detail'),
    path('Add_the_order_to_the_users_order_list/', views.Add_the_order_to_the_users_order_list, name='Add_the_order_to_the_users_order_list'),
]