from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutTheCompanyPageView(TemplateView):
    template_name = 'about_the_company.html'

class CompanyReviewsPageView(TemplateView):
    template_name = 'company_reviews.html'