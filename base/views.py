from django.http import HttpRequest, HttpResponse, JsonResponse
import json

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

def forPost(request: HttpRequest):
    if request.method == 'POST':
        data = request.body.decode()
        print(json.loads(data))

        return JsonResponse(json.loads(data))
        
    if request.method == 'GET':
        print('GET')
        print(request.headers['User-Agent'])

        return HttpResponse("Hi Bro")
