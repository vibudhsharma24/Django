from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("you are at website home page")
    #return render(request, 'index.html')##abhi iss se template load nahi hua dna error aa gya hai website pe
    ## error fix: settings mei jaake directory mei bas path daal dena ki kahan se kya aa rha hai 
    return render(request, 'website/index.html') ##kyunki ab index vaali filr website ke folder mei hai so basically bas path define kara hai 
    

def about(request):
    return HttpResponse("you are at website about page")

def contact(request):
    return HttpResponse("you are at website contact page")
##ye def functions ke naam kuch bhi ho sakte hai 
