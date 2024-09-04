from django.shortcuts import render
from .models import NamesList, DevCommunity
from django.shortcuts import get_object_or_404
from .forms import NameListForm

# Create your views here.
def all_names(request):
    #Fetch all data from the db
    names = NamesList.objects.all()
    return render(request, 'mibits/all_name.html', {'names': names})

def name_detail(request, name_id):
    name = get_object_or_404(NamesList, pk=name_id)
    return render(request, 'mibits/name_detail.html', {'name': name})

def dev_community_view(request):
    communities = None
    if request.method == 'POST':
        form = NameListForm(request.POST)
        if form.is_valid():
            name_list = form.cleaned_data['name_list']
            communities = DevCommunity.objects.filter(name_lists= name_list)
    else:
        # create a blank form to render
        form = NameListForm() 
    
    return render(request, 'mibits/dev_community.html', {'communities': communities, 'form': form})

