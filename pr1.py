# Nombre: Martínez Martínez Nicolás
# Boleta: 2025640187
# Número de Práctica: 1
# Fecha: 08/09/25

#Bibliotecas utilizadas
import numpy as np
import random
import os
import sys

#Lista para almacenar num ingresados por el usuario
numeros=[]

#Menu
op = int(input("Mi programa \n 1. Media Aritmetica \n 2. Desviacion Estandar \n 3. Burbuja \n 4. Salir \n Escriba la opcion que desea: \n"))

#Opcion 1: Media Aritmetica
if op ==1 :
    print("\nSelecciono Media Aritmetica\n")
    print("Ingresa tantos numero quieras hasta ingresar una 'x' \n") 
    
    #Ciclo para que se capturen los x numeros que el usuario decida
    while True:
        num = input("Numero: ")
        if num.lower() == "x" : #hasta que ponga una x se termina el registro
            break
        if num != "x": 
            num = float(num) #los conierte a float
            numeros.append(num) #los agrega a la lista

    #Si el numero de elementos en la lista es mayor  a cero, calcula la media
    if len(numeros) > 0:
        media = np.mean(numeros) #Usando funcion '.mean' para el calculo de la media 
        print(f"La media es: ",media)
    else:
        #Mensaje de error
        print("Error")


#Opcion 2: DEsviacion Estandar
elif op== 2 :
    print("\nSelecciono Desviacion Estandar\n")
    print("Ingresa tantos numero quieras hasta ingresar una 'x' \n") 
    
    #Ciclo para capturar los numeros que ingrese el usuario
    while True:
        num = input("Numero: ")
        if num.lower() == "x" : #hasta que ponga una x se termina el registro
            break
        if num != "x":
            num = float(num) #los conierte a float
            numeros.append(num) #los agrega a la lista

    #Si el numero de elementos en la lista es mayor  a cero, calcula la media
    if len(numeros) > 0:
        std = np.std(numeros) #Usando funcion '.std' para el calculo de la desviacion estandar 
        print(f"La desviacion estandar es: ",std)
    else:
        #Mensaje de error
        print("Error")

#Opcion 3: Ordenamietno Burbuja
elif op == 3:
    print("\nSelecciono Burbuja\n")
    print("Ingresa tantos numero quieras hasta ingresar una 'x' \n") 
    n = int(input("Ingresa el número de muestras: \n")) #Numero de de muestras para que sean generadas
    
    #Genera lista con numeros aleatorios en cierto rengo
    for i in range(n):
        numeros.append(random.randint(1, 100))  #Genera un numero aleatorio en el rango [1,100]
        
    #Algoritmo Brubuja (De mayor a menor)
    print("Arreglo generado:", numeros)
    for i in range(len(numeros)):
        for j in range(len(numeros)-1):
            if numeros[j] < numeros[j+1]:  
                temp = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = temp

    print("Arreglo ordenado de mayor a menor:", numeros)
   
   #Salida 
elif op == 4:
    print("Adiosss")
    sys.exit() #Finaliza el programa

else:
    print("No existe :(")
    os.system('cls') #Limpia la pantalla
    