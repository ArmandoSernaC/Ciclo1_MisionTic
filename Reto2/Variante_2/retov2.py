import numpy as np
from math import sqrt

def reto2(a):
  """
  L = (n*(n+1))/2
  2*L = n*(n+1)
  2*L = n**2 + n 
  0 = n**2 + n - 2*L 

  Ecuación cuadrática 
  (-b +/- ((b**2 ) - 4*a*c)**(1/2))//2a

  a = 1
  b = 1
  c = -2*L

  n = (-1 + (1 + 8*L)**(1/2))//2 

  """
  L = len(a)
  n = int(round((-1 + (1 + 8*L)**(1/2))/2))
 
  matriz = np.zeros((n, n))
  k  = 0
  for i in range(n):
    for j in range (i+1):  
      if k <L:
        matriz[i][j] = l[k]
        k += 1
  return matriz
