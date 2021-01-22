from __future__ import print_function
from ortools.linear_solver import pywraplp
import numpy as np

def CargaMP(nombreMP, cantMP, porcPerdida):
  i=0
  print("Ingrese nombre de materia prima")
  var=input()
  while (var!="fin"):
    nombreMP.append(var)
    print("Ingrese cantidad disponible")
    cantMP.append(int(input()))
    print("Ingrese porcentaje de pérdida")
    porcPerdida.append(float(input()))
    i=i+1
    print("Ingrese nombre de materia prima, para finalizar ingrese fin")
    var=input()

def CargaHelados(SaboresH, PrecioH):
  i=0
  print("Ingrese sabor de helado")
  var=input()
  while (var!="fin"):
    SaboresH.append(var)
    print("Ingrese precio")
    PrecioH.append(int(input()))
    i=i+1
    print("Ingrese sabor de helado, para finalizar ingrese fin")
    var=input()

'''def ObtnerCoef(nombreMP, SaboresH, filas, columnas):
  val=(filas,columnas) 
  Matriz=np.empty(val)
  print(Matriz)
  arre=np.empty(columnas-1)
  for i in range(filas):
    print("Para la MP ", nombreMP[i]," ingrese el consumo por sabor de helado:")
    for j in range(columnas):
      print("",SaboresH[j])
      coef=input()
      Matriz=np.
  

  return Matriz
'''
nombreMP=[]
cantMP=[]
porcPerdida=[]
# CargaMP(nombreMP,cantMP,porcPerdida)
# filas=len(nombreMP)
SaboresH=[]
PrecioH=[]
# CargaHelados(SaboresH,PrecioH)
# columnas=len(SaboresH)
#valores=list(map(int, input("Introduzca coeficientes: ").split()))
#MCoef=np.array(valores).reshape(filas, columnas)


#MCoef=ObtnerCoef(nombreMP, SaboresH, filas, columnas)


def create_data_model ():
  data={}
  data['constraint_coeffs']=[[10],[6]]#Cant de MP usada para hacer el helado. matriz: materia prima x helado
  data['perdida']=[[0.1],[0.3]]#Perdida por materia prima, 1 fila, 2 columnas
  data['bounds2']=[0.7,0.9]#Máxima perdida que se puede tener
  data['bounds']=[20000,10000]#MP disponible
  data['obj_coeffs']=[70]#Precio de helados
  data['num_vars']=1#N° helados
  data['dinero_MP']=[10,5] #Dinero que cuesta cada MP por unidad
  data['num_constraints']=2#N° de MP
  data['demanda']=[200]
  return data

#inciamos el modelo
data = create_data_model()
solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#cargamos las variables de decision
x = {}
for j in range(data['num_vars']):
    x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo

print('Number of variables =', solver.NumVariables())
print(nombreMP)
print(cantMP)
print(porcPerdida)
print(SaboresH)
print(PrecioH)

#cargamos restricciones
for i in range(data['num_constraints']):
  constraint = solver.RowConstraint(0, data['bounds'][i], '') #Selecciona la cant disponible de mp
  for j in range(data['num_vars']):
    constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

#Restriccion de que la produccion debe ser mayor o igual que la demanda
for i in range(data['num_vars']):
  constraint = solver.RowConstraint(data['demanda'][i], float('inf') , '')
  for j in range(solver.NumVariables()):
    constraint.SetCoefficient(x[j],1) 

#cargamos objetivo
objective = solver.Objective()
for j in range(data['num_vars']):
  objective.SetCoefficient(x[j], 1)
objective.SetMaximization()

# MAXIMIZACION DE LA PRODUCCION
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
  print('Objective value =', solver.Objective().Value())
  for j in range(data['num_vars']):
    print(x[j].name(), ' = ', x[j].solution_value())
  print()
else:
  print('The problem does not have an optimal solution.')
