# HABLAR CON EL JOAQUIN, ¿QUE COSTOS MINIMIZAR?
from __future__ import print_function
from ortools.linear_solver import pywraplp


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

def minimizacion_costos(data):
    #inciamos el modelo
    #data = create_data_model()
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

    respuesta = ""
  # MINIMIZACION DE COSTOS
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta+=str(x[j].name(), ' = ', x[j].solution_value()) + "\n"
    else:
        print('The problem does not have an optimal solution.')
        respuesta+= "No hay solucion optima. \n"
    return respuesta


def maximizacion_ganancias(data):
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo

    print('Number of variables =', solver.NumVariables())
    #print(nombreMP)
    #print(cantMP)
    #print(porcPerdida)
    #print(SaboresH)
    #print(PrecioH)

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
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMaximization()

    #Si se minimiza da 0, no minimizar 

    # MAXIMIZACION DE LAS GANANCIAS
    status = solver.Solve()

    respuesta = ""

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta+=str(x[j].name(), ' = ', x[j].solution_value()) + "\n"
    else:
        print('The problem does not have an optimal solution.')
        respuesta+= "No hay solucion optima. \n"
    return respuesta




def maximizacion_produccion(data):
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo


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

    respuesta = ""
    # MAXIMIZACION DE LA PRODUCCION
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta+=str(x[j].name(), ' = ', x[j].solution_value()) + "\n"
    else:
        print('The problem does not have an optimal solution.')
        respuesta+= "No hay solucion optima. \n"
    return respuesta
