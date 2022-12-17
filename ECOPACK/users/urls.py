from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.Registration.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ViewUsersProfile.as_view(), name='profile')
]