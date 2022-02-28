from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# for home
def index(request):
    return render(request, 'index.html')
def add_banner(request):
    pass
def add_banner_content(request):
    pass