from django.shortcuts import render
from django.http import HttpResponse
from.import models
from.models import company

# Create your views here.
def index(request):
    return HttpResponse('<html><head><title>nervana</title></head><body><h2><a href="/form_company"> go to entry data</a></h2> <br/><h2><a href="/showData"> go to dat show</a></h2></body></htm>')

def create_company(request):
    return render (request,'form_create.html',{})

def backend1(request):
    new=models.company()
    v1=request.POST['fullname']
    v2=request.POST['email']
    v3=request.POST['age']
    v4=request.POST['date']
    new.fullname=v1
    new.email=v2
    new.age=v3
    new.birhday=v4

    new.save()
    return showData(request)


def showData(request):
    data = company.objects.all()
    return render(request,'showData.html',{'d':data})


def backend2(request,id):
    new=models.company()
    v0 = id
    v1=request.POST['fullname']
    v2=request.POST['email']
    v3=request.POST['age']
    v4=request.POST['date']
    new.id=v0
    new.fullname=v1
    new.email=v2
    new.age=v3
    new.birhday=v4

    new.save()
    return showData(request)

def updateData(request,id):

    return render(request,'updateData.html',{'id':id})