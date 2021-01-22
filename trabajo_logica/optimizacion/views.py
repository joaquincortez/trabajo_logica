from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CalculosForm
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado
import json
from .calculos import producto, calcular_precios_helado, calcular_precios_materia,datos_helados,datos_materiaprima_helado,datos_materias, mapaea_materias, crear_modelo


def index(request):
    return render(request, 'optimizacion/index.html')

def optimizacion(request):
    return render(request, 'optimizacion/optimizacion.html')

def calculos_helado(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #print(body)
        resultado = calcular_precios_helado(body)
        #print(resultado)
        id_helados,cantidades, precios, demandas = datos_helados(body)
        cant_mph = datos_materiaprima_helado(id_helados)
        #print("id helados son: %s \n cantidades son %s \n precios son %s \n demandas son %s \n cant materia prima por helado es %s"  %(str(id_helados),str(cantidades), str(precios), str(demandas), str(cant_mph)))
        return JsonResponse(resultado)

def calculos_materia(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #print(body)
        resultado = calcular_precios_materia(body)
        #print(resultado)
        id_materias, disponibilidad, costos = datos_materias(body)
        #print("id materias son: %s \n disponibilidades son %s \n costos son %s "  %(str(id_materias),str(disponibilidad), str(costos)))

        return JsonResponse(resultado)

def calculos(request):
    if request.method == 'POST':
        print("ACAAAAAAAAAAAAA")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        helados = body["helados"]
        id_helados,cantidades, precios, demandas = datos_helados(helados)
        cant_helados = len(id_helados)
        cant_mph = datos_materiaprima_helado(id_helados)
        print("ACA id helados son: %s \n cantidades son %s \n precios son %s \n demandas son %s \n cant materia prima por helado es %s"  %(str(id_helados),str(cantidades), str(precios), str(demandas), str(cant_mph)))

        materias = body["materias"]
        id_materias, disponibilidad, costos = datos_materias(materias)
        print(" ACA id materias son: %s \n disponibilidades son %s \n costos son %s "  %(str(id_materias),str(disponibilidad), str(costos)))

        arreglo_mat_helado = mapaea_materias(id_materias,cant_helados,cant_mph)
        print("arreglo es %s" %arreglo_mat_helado)

        

        return HttpResponse("xd")


class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()