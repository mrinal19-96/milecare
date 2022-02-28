from django.http import HttpResponse
from django.shortcuts import render

# home page
def homepage(request):
    return render(request, "index.html")
    # return HttpResponse("hi")

# about Page
def aboutpage(request):
    return render(request, 'about.html')

# team Page
def teampage(request):
    return render(request,'team.html')

# contact Page
def contactpage(request):
    return render(request, 'contact.html')
