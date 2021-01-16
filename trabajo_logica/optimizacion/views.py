from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CalculosForm
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado


def index(request):
    return render(request, 'optimizacion/index.html')

def optimizacion(request):
    
    return render(request, 'optimizacion/optimizacion.html')

def calculos(request, service):
    return HttpResponse('Hola servicio {{servicio}}')

def calculos(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/gracias/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculosForm()

    return render(request, 'optimizacion/calculos.html', {'form': form})

class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()