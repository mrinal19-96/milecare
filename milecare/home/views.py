from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeBanner, HomeBoxSection, HomeProductivity

# for home
def home(request):
    banner_data = HomeBanner.objects.all()
    banner_box = HomeBoxSection.objects.all()
    product_section = HomeProductivity.objects.all()
    return render(request, 'home/home.html', {'banner_data':banner_data, 'banner_box':banner_box, 'product_section':product_section})
def add_banner(request):
    pass
def add_banner_content(request):
    pass