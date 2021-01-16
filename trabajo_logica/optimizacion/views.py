from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CalculosForm
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado


def index(request):
    return render(request, 'optimizacion/index.html')

def optimizacion(request):
    return render(request, 'optimizacion/optimizacion.html')

def calculos(request):
    if request.method == 'POST':
        return HttpResponse('hola xdxxd')


class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()