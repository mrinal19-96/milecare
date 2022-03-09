from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeBanner, HomeBoxSection, HomeProductivity, HomeInterface

# for home
def home(request):
    banner_data = HomeBanner.objects.all()
    banner_box = HomeBoxSection.objects.all()
    product_section = HomeProductivity.objects.all()
    service_section = HomeInterface.objects.all()
    context =  {'banner_data':banner_data,
                   'banner_box':banner_box, 
                   'product_section':product_section,
                   'service_section':service_section,
                   }
    return render(request, 'home/home.html',context)
def add_banner(request):
    pass
def add_banner_content(request):
    pass