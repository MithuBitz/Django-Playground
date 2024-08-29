from django.shortcuts import render
from .models import NamesList
from django.shortcuts import get_object_or_404

# Create your views here.
def all_names(request):
    #Fetch all data from the db
    names = NamesList.objects.all()
    return render(request, 'mibits/all_name.html', {'names': names})

def name_detail(request, name_id):
    name = get_object_or_404(NamesList, pk=name_id)
    return render(request, 'mibits/name_detail.html', {'name': name})