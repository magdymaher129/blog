from django.shortcuts import render
from science import models
from .models import book

    


def index(request):
    posts=book.objects.all()
    return render(request,'base.html',{'posts':posts})


