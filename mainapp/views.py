from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = {"email":email , "password" : password}
            return JsonResponse(data)
    #Get goes here
    return render(request,'base.html')

# Create your views here.
