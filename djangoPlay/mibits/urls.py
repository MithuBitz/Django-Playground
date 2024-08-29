
from django.urls import path, include

from . import views

urlpatterns = [    
    path('', views.all_names, name='all_names'),      
    path('<int:name_id>/', views.name_detail, name='name_detail'),
]