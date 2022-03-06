from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeBanner
# Create your views here.

# for home
def home(request):
    banner_data = HomeBanner.objects.all()
    return render(request, 'home/home.html', {'banner_data':banner_data})
def add_banner(request):
    pass
def add_banner_content(request):
    pass