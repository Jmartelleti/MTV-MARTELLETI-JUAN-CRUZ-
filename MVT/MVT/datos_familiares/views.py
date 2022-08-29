from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context, Template
from .models import Familiar

# Create your views here.
def Datos_familiares (request):
    Datos_Listados = Familiar.objects.all()
    # Datos_Listados = {"Familiares": Familiar.objects.all()}
    return render(request, "template1.html",{"Familiares": Datos_Listados})
    # Plantilla = loader.get_template("template1.html")
    # documento_html = Plantilla.render(Datos_Listados)
    # return HttpResponse(documento_html)