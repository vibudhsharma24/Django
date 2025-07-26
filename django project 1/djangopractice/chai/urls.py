
from django.urls import path 
from . import views ##. is current directory
urlpatterns = [
    path('', views.all_chai, name='all_home'), 
    #path('chai/', include('chai.urls')),  ##ye hamare app vala urls hai
] 