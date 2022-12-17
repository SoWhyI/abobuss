from django.urls import path
from . import views
from .views import image_request

urlpatterns = [
    path('', views.List_of_products, name='list_of_products'),
    path('new/',  image_request, name='product_creation'),
    path('<int:pk>/delete/', views.ProductRemoveView.as_view(), name='product_remove'),
    path('<int:pk>/edit/', views.ProductChangesView.as_view(), name='product_changes'),
    ]