# Nombre: Martínez Martínez Nicolás
# Boleta: 2025640187
# Número de Práctica: 1
# Fecha: 08/09/25

#Bibliotecas utilizadas
import numpy as np
import os
import sys
#Menu
op = int(input("Mi programa \n 1.Opcion Directa\n 2.Ingresar Ecuaciones \n 3.Salida\n Escriba la opcion que desea: \n"))
#Resuelve de manera directa el sistema de ecuaciones prefedinido 
if op==1:
    
    #Definimos la matriz A (x,y,z)
    A=np.array([[2,-4,-3],[1,5,-5],[4,2,67]])
    #Definimos el vector B (Constantes)
    B=np.array([15,5,20])
    #Resuelve el sistema Ax=B
    x=np.linalg.solve(A,B)
    print(x)
#Permite al ususario ingresar un sistema de ecuaciones
elif op==2:
    print("Escriba cada fila entre corchetes. Ejemplo: [2, -4, -3]")

    #El usuario ingresa las 3 filas de la matriz A
    A=np.array(eval(input("Ingrese Fila 1: \n")))
    B=np.array(eval(input("Ingrese Fila 2: \n")))
    C=np.array(eval(input("Ingrese Fila 3: \n")))
    
    D=np.vstack([A,B,C]) #Crea la matriz, uniendo los vectores de forma vertical
    
    print("\nEscriba el vector entre corchetes. Ejemplo: [2, -4, -3]\n")
    E=np.array(eval(input("Ingrese vector B: \n"))) #El usuario ingresa los valores para el vector B
    x=np.linalg.solve(D,E) #Resuelve el sistema Ax=B
    #Imprime cada incognita por separado
    print("x: ", x[0])
    print("y: ", x[1])
    print("z: ", x[2])
    
#Sale del programa
elif op == 3:
    print("Adiosss")
    sys.exit()

#Opcion Invalida
else:
    print("No existe :(")
    os.system('cls') #Limpia la pantalla
