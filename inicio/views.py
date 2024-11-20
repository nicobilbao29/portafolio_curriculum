from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Bienvenido a mi portafolio")


from django.shortcuts import render

def index(request):
    return render(request, 'inicio/index.html')
