from .models import Helado, MateriaPrima, MateriaPrima_Helado
import numpy as np


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

def datos_helados(datos):
    lista = list(datos.items())
    cantidades = list(datos.values())
    precios = []
    demandas = []
    
    for key, value in lista:
        helado = Helado.objects.get(id=key)
        precios.append(float(helado.precio))
        demandas.append(value)
    
    return list(datos.keys()),cantidades, precios, demandas


def datos_materias(datos):
    id_materias = list(datos.keys())
    costos = []
    for idm in id_materias:
        costos.append(float(MateriaPrima.objects.get(pk=idm).costo))
    return list(map(int, id_materias)), list(datos.values()), costos

def datos_materiaprima_helado(helados_id):
    cantidades_mph = [] #mph: materia prima por helado
    
    for helado in helados_id:
        materias_helado = {}
        mphs = MateriaPrima_Helado.objects.all().filter(helado = helado)
        for m in mphs:
            materias_helado[m.materia_prima.id] = m.cantidad
        cantidades_mph.append(materias_helado)
    
    return cantidades_mph


def mapaea_materias(id_materias,cant_helados, reg_mat_hel):
    cant_materias = len(id_materias)
    arr_cant_mathelado = np.zeros((cant_materias, cant_helados), dtype=int)
    for i in range(0,cant_materias):
        print("\n\n\n MATERIA %s" %i)
        for j in range(0,cant_helados):
            print("\n HELADO %s" %j)
            mat_helados = list(reg_mat_hel[j].keys())
            cant_mat_helado = list(reg_mat_hel[j].values())
            print("ID MATERIAS ES %s" %id_materias)
            print("ID MATERIAS DEL HELADO ES ES %s" %mat_helados)
            print("CANT MATERIAS DEL HELADO ES ES %s" %cant_mat_helado)
            l=0
            while(l < len(mat_helados) and id_materias[i] != mat_helados[l]):
                l+=1
            if l != len(mat_helados):
                print("ARREGLO ANTES ESCRIBIR ES %s" %arr_cant_mathelado.tolist())
                print("SE ESCRIBIO ARREGLO[%s][%s] = %s" %(i,j,cant_mat_helado[l]))
                arr_cant_mathelado[i][j]= cant_mat_helado[l]
    
    return arr_cant_mathelado.tolist()

def crear_modelo(precio_helados, demanda_helados, mat_helado, disponibilidad_materias, costo_materias):
    data={}
    data['constraint_coeffs']=mat_helado #Cant de MP usada para hacer el helado
    data['bounds']=disponibilidad_materias #MP disponible
    data['obj_coeffs']=precio_helados #Precio de helados
    data['num_vars']= len(precio_helados)#N° helados
    data['precio_base']=costo_materias #Dinero que cuesta cada MP por unidad
    data['num_constraints']=len(costo_materias) #N° de MP
    data['demanda']=demanda_helados
    return data


