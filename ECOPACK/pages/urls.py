from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutTheCompanyPageView.as_view(), name='about'),
    path('company_reviews/', views.CompanyReviewsPageView.as_view(), name='reviews'),
]