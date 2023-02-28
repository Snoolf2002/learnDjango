from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse, JsonResponse

def index(request:HttpRequest):
        a = request.GET.get('a')
        b = request.GET.get('b')

        if a!=None and b!=None:    
            return HttpResponse(f"{a}+{b}={int(a)+int(b)}")
        
        return HttpResponse("Hey you must give two numbers")

def forJsonResponse(request:HttpRequest):
    a = request.GET.get('a')
    b = request.GET.get('b')

    if a!=None and b!=None:  
        return JsonResponse({
            'result': f"{a}+{b}={int(a)+int(b)}"
        })
    return HttpResponse("Hey you must give two numbers")

urlpatterns = [
    path('', index),
    path('salom/', forJsonResponse)
]
