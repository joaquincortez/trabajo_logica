from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado
import json
from .calculos import calcular_precios_helado, calcular_precios_materia,datos_helados,datos_materiaprima_helado,datos_materias, mapaea_materias, crear_modelo, encuentra_no_validos
from .calculos_or import minimizacion_costos, maximizacion_ganancias, maximizacion_produccion


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
        #id_helados,cantidades, precios, demandas = datos_helados(body)
        #cant_mph = datos_materiaprima_helado(id_helados)
        #print("id helados son: %s \n cantidades son %s \n precios son %s \n demandas son %s \n cant materia prima por helado es %s"  %(str(id_helados),str(cantidades), str(precios), str(demandas), str(cant_mph)))
        return JsonResponse(resultado)

def calculos_materia(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #print(body)
        resultado = calcular_precios_materia(body)
        #print(resultado)
        #id_materias, disponibilidad, costos = datos_materias(body)
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

        #Elimino los que no son posibles crear ya que no se seleccionaron todas sus materias primas como disponibles.
        no_validos, id_no_validos = encuentra_no_validos(id_materias,cant_mph, id_helados)
        print(" no validos es %s" %no_validos)
        for i in range(0,len(no_validos)):
            print(" i es %s" %i)
            print("no_validos[%s] es %s" %(i,no_validos[i]))
            print("precios son %s demandas son %s y arreglo mat helado son %s" %(precios,demandas,arreglo_mat_helado))
            del precios[no_validos[i]]
            del demandas[no_validos[i]]
            for j in range(0, len(id_materias)):
                del arreglo_mat_helado[j][no_validos[i]]
            for j in range(i+1, len(no_validos)):
                no_validos[j]=no_validos[j] -1
            print("precios son %s demandas son %s y arreglo mat helado son %s" %(precios,demandas,arreglo_mat_helado))
            print(" no validos es %s" %no_validos)
            print("no_validos[%s] es %s" %(i,no_validos[i]))


        data = crear_modelo(precios,demandas, arreglo_mat_helado, disponibilidad,costos)
        respuesta = ""
        for idh in id_no_validos:
            print("No es posible producir %s " %Helado.objects.get(pk=idh).nombre)
            respuesta += ("No es posible producir %s \n" %Helado.objects.get(pk=idh).nombre)

        print("minimizacion costos")
        respuesta +="minimizacion costos"
        respuesta +=minimizacion_costos(data)
        print("maximizacion ganancias")
        respuesta +="maximizacion ganancias"
        respuesta +=maximizacion_ganancias(data)
        print("maximizacion produccion")
        respuesta +="maximizacion produccion"
        respuesta +=maximizacion_produccion(data)
        #QUEDA ELIMINAR LOS HELADOS PARA LOS QUE NO TENGO LAS MATERIAS PRIMAS E INFORMAR QUE NO SE PUEDE PRODUCIR
        #PARA ESTO PIENSO QUE LO IDEAL SERIA UNA VEZ HECHOS TODOS LOS CALCULOS ANTERIORES,
        #SE EVALUEN SI LAS MATERIAS DEL HELADO ESTAN CONTENIDAS EN LAS MATERIAS SELECCIONADAS
        #SI NO LO ESTA SE ELIMINAN LOS DATOS, EN EL INDICE, DE CADA UNO DE LOS ARREGLOS.

        return HttpResponse(respuesta)



class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()