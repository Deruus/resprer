from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def restaurantes(request):
    return render(request,'restaurantes.html')
def reservar(request):
    return render(request,'reservar.html')
def login(request):
    return render(request,'login.html')
def contacto(request):
    return render(request,'contacto.html')