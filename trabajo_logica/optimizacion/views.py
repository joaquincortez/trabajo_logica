from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CalculosForm
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado
import json
from .calculos import producto, calcular_precios_helado, calcular_precios_materia


def index(request):
    return render(request, 'optimizacion/index.html')

def optimizacion(request):
    return render(request, 'optimizacion/optimizacion.html')

def calculos_helado(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        resultado = calcular_precios_helado(body)
        print(resultado)
        return JsonResponse(resultado)

def calculos_materia(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        resultado = calcular_precios_materia(body)
        print(resultado)
        return JsonResponse(resultado)


class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()