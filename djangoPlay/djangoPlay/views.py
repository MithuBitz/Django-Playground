from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Home: Its a Django Playground")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("About: Its a Django Playground")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Contact: Its a Django Playground")
    return render(request, 'website/contact.html')