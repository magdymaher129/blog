from django.shortcuts import render
from django.http import HttpResponse
from.import models
posts=[
    {'age':21,
     'address':'sohag',
     'name':'Omar',
        },{
            'age':51,
     'address':'qena',
     'name':'Ali',
            
        }
]

def index(request): 
     
    return render(request,'base1.html',{'posts':posts} )



