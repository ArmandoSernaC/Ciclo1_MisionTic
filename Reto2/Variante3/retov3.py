
def CuadradosPerfectos(Matriz):
  n = len(Matriz)
  CantidadCP = 0
  cuadradosPerfectos = []

  for i in range (n):
    for j in range (n):      
      x = ((Matriz[i][j])**(1/2))%1 
     
      if x == 0.0 :
        CantidadCP += 1
        cuadradosPerfectos.append(Matriz[i][j])

  return  CantidadCP, cuadradosPerfectos


