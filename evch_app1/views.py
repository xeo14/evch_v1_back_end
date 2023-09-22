from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vistaUno(request):
    a="""
    Hola Mundo, esta es la pagina 1
    """

    b="""
    como estas?
    """


    return HttpResponse(a,b)