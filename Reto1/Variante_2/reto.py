from vector import vector
import random
import math


 

def solucion():
  
    
    
    a = random.randint(15,30)     
    v = vector(a)
   
    
    for i in range(1, a+1):        
        v.V[i] = random.randint(1,9999)#Completar
        
    s = 0  
    for i in range(1,v.V[0]):  
        if es_primo(v.V[i] ) or comienza_digito_impar(v.V[i]): #Completar
            s += v.V[i]
            
       
    return v, s

  
def es_primo(n):
  
    """
    Esta función retorna True si el número n es primo
    Retorna False si el número n NO es primo
    
    -Un número primo es un número que SOLO es divisible por él mismo y el 1.
    Ejemplos: 2, 3, 5, 7, 11, 13, y el 17 son números primos.
    
    -Un número k es divisible por d si k módulo d es cero: k % d == 0
    Ejemplos:8 es divisible por 4, 9 es divisible por 3, 27 es divisible por 3.
    
    Comprobemos si el número n es un número primo, para ello se hará lo siguiente:
        Probar si n es divisible por un número entre 2 y n-1.
        En caso de que NO haya ningún número tal que n sea divisible por él, retornamos True (Sí es primo), pero si hay 
        al menos UN número en ese intervalo que divida a n, retornamos False (No es primo) """
    
    for d in range(2, n-1):          
        if n%d == 0 :
          return False
            
    """Si logra salir de este ciclo, es porque no hayó ningún número que divida a n, por tanto SÍ es primo"""
   
    return True
    

def comienza_digito_impar(n):
  
    """Esta función retorna True si n comienza por un dígito impar, ejemplo de números que
    comienzan por dígito impar: 1234, 76555, 92228
    Retorna False si n NO comienza por dígito impar"""
    
    
    d = str(n)[0]     
    d = int(d)    
    
    if d % 2 == 1:    
      
        """Si entra a este condicional, es porque n empieza por un dígito impar"""
        return True
        
    """Si NO entra al condicional anterior, es porque n NO empieza por un dígito impar"""    
    return False
      
    
"""Esta función permite imprimir vectores en la consola"""

def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()
    
"""Las siguientes líneas le permitirán probar su solución al presionar el botón de ejecutar"""
a, suma = solucion()
imprimeVector(a, 'Original')
print("Suma: ", suma)
