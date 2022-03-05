from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# for home
def home(request):
    return render(request, 'home/home.html')
def add_banner(request):
    pass
def add_banner_content(request):
    pass