from django.shortcuts import render
from arabic.models import info



def index(request):
    posts=info.objects.all()
    
    
    return render(request,'base2.html',{'posts':posts})
