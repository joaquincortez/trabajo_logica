from .models import Helado, MateriaPrima, MateriaPrima_Helado

def producto(a,b):
    return a * b

def calcular_precios_helado(datos):
    lista = datos.items()
    resultado = {}
    total = 0
    print(lista)
    print(type(lista))
    for key, value in lista:
        helado = Helado.objects.get(id=key)
        precio = helado.precio * int(value)
        resultado[helado.nombre] = str(precio) #precio * cant
        total+= precio
    resultado["total"] = str(total)
    return resultado

def calcular_precios_materia(datos):
    lista = datos.items()
    resultado = {}
    total = 0
    print(lista)
    print(type(lista))
    for key, value in lista:
        materia_prima = MateriaPrima.objects.get(id=key)
        precio = materia_prima.costo * int(value)
        resultado[materia_prima.nombre] = str(precio) #precio * cant
        total+= precio
    resultado["total"] = str(total)
    return resultado