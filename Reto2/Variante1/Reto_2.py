import numpy as np

def solucion(A):
  nn = len(A)
  menor  = 1000000
  posicion = []

  for i in range (nn):
     for j in range (nn-i):
       if A[i,j] <= menor and (j+i)%2 == 1 :     
         menor = A[i,j]
         

  for m in range (nn):
    for n in range (nn-m):
      if A[m,n] == menor :      
        posicion.append([m,n])

  return menor, posicion






  return n
