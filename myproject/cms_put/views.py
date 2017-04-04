from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.

def nuevonombre(request, uno, dos):
    if request.method == "POST":
        uno = request.POST['name']
        dos = request.POST['page']
        pag = Pages(name=uno, page=dos)
        pag.save()
        return HttpResponse("Nombre incluido correctamente")
    elif request.method == "PUT":
        cuerpo = request.body.decode('utf-8')
        uno, dos = cuerpo.split(",")
        pag = Pages(name=uno, page=dos)
        pagina.save()
        return HttpResponse("Nombre incluido correctamente")
    else:
        respuesta = "Operacion no valida"
        return HttpResponse(respuesta)

def lista_paginas(request):
    lista_pages = Pages.objects.all()
    respuesta = "<ol>"
    for pages in lista_pages:
        respuesta += '<li><a href= "' + pages.name + '">' + pages.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

def pages(request, ident):
    if request.method == "GET":
        try:
            page = Pages.objects.get(name = ident)
            respuesta = page.page
        except Pages.DoesNotExist:
            respuesta = "El nombre no existe. Prueba otra vez."
            return HttpResponse(respuesta)
    else:
        respuesta = "Operacion no valida"
        return HttpResponse(respuesta)

def mi404(request):
    return HttpResponse("No tenemos lo que nos pides. Prueba otra vez.")
