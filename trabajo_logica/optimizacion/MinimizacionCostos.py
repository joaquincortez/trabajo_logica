# HABLAR CON EL JOAQUIN, ¿QUE COSTOS MINIMIZAR?
from __future__ import print_function
from ortools.linear_solver import pywraplp

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
#filas=len(nombreMP)
SaboresH=[]
PrecioH=[]
# CargaHelados(SaboresH,PrecioH)
#columnas=len(SaboresH)
#valores=list(map(int, input("Introduzca coeficientes: ").split()))
#MCoef=np.array(valores).reshape(filas, columnas)


#MCoef=ObtnerCoef(nombreMP, SaboresH, filas, columnas)

materias_disponibles_id= [1,2,3,4,5]
materias_disponibles_cant = [500,200,100,300,400]

cada_helado = [3,5,8,4,0]
cada_helado


def create_data_model ():
    data={}
    data['constraint_coeffs']=[[10,8],[6,2]]#Cant de MP usada para hacer el helado
    data['bounds']=[20000,10000]#MP disponible
    data['obj_coeffs']=[70,50]#Precio de helados
    data['num_vars']=2#N° helados
    data['precio_base']=[20,10] #Dinero que cuesta cada MP por unidad
    data['num_constraints']=2#N° de MP
    data['demanda']=[100,100]
    return data

def trabaja():
    #inciamos el modelo
    data = create_data_model()
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo

    print('Number of variables =', solver.NumVariables())
    # print(nombreMP)
    # print(cantMP)
    # print(porcPerdida)
    # print(SaboresH)
    # print(PrecioH)

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
        objective.SetCoefficient(x[j], data['precio_base'][j])
    objective.SetMinimization()


  # MINIMIZACION DE COSTOS
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
    else:
        print('The problem does not have an optimal solution.')

trabaja()


