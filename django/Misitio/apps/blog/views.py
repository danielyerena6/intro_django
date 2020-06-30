from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Lenguajes de Internet</h1> Alumno: Carlos Daniel Yerena Mercado <br> Grupo: 8CM11")