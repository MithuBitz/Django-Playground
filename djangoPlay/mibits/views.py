from django.shortcuts import render

# Create your views here.
def all_names(request):
    return render(request, 'mibits/all_name.html')