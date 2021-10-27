from abc import abstractclassmethod
import asyncio
from asyncio.tasks import sleep
import random
import os
from types import new_class

path = 'D:/Estudio/Python'      																	#Directorio 
os.chdir(path)
  
with open('vehiculos.txt', 'w') as fp: 														#Crea el archivo o borra lo que tiene
    pass

async def Semaforo(u_input):    
    print("Rojo\n") 
    for i in range (u_input):																					
        with open('vehiculos.txt', 'a') as fp: 
            pass
            ciclo = "ciclo "
            numero = str(i+1)
            texto = ciclo + numero
            fp.write(texto) 
        print ("Inicia el semáforo vertical (ciclo ", i+1, ')')      
        with open('vehiculos.txt', 'a') as fp: 
            pass
            fp.write("\nsemáforo vertical\n")  
        print ("\nAmarillo")																			#Espera el amarillo del semáforo vertical
        await asyncio.sleep(3)
        await S_vertical()            														#Espera a que termina el semáforo vertical
        print ("\nInicia el semáforo horizontal")
        print ("\nAmarillo")
        await asyncio.sleep(3)         													  #Cuenta el ciclo de amarillo, del semáforo horizontal
        with open('vehiculos.txt', 'a') as fp: 										#Añade información al archivo 
            pass
            fp.write("\nsemáforo horizontal\n")
        await S_horizontal()
    with open('vehiculos.txt', 'r') as fp: 												#Cuando acaba los ciclos lee el archivo, con la información de los autos
        pass
        print(fp.read())

async def carros():
    b = 0
    while b < 7:                        												   #Cuenta los segundos que tarda. El ciclo de verde tarda 6 segundos,
        a = random.randint(1,3)																		 #por lo que hay una probabilidad de que alguien pase en amarillo mas no en rojo, añadido para más realismo xD
        if a == 1:
            print ("paso un carro")
            with open('vehiculos.txt', 'a') as fp:								 #Añade información al archivo 
                pass
                fp.write("  carro\n")
            b += 1
            await asyncio.sleep(1)      													 #Espera a que pase el vehículo
        elif a == 2:
            print ("paso un bus")
            with open('vehiculos.txt', 'a') as fp:								 #Añade información al archivo 
                pass
                fp.write("  bus\n")
            b += 2
            await asyncio.sleep(2)
        elif a == 1:
            print ("paso un camión")
            with open('vehiculos.txt', 'a') as fp:								 #Añade información al archivo 
                pass
                fp.write("  camión\n")
            b += 3
            await asyncio.sleep(3)

async def S_vertical():     
    print("\nVerde \n")
    task = asyncio.create_task(carros())  												 #Hace una tarea en simultaneo que cuenta carros
    await asyncio.sleep(6)               													 #Espera a que cuente 6 para cambiar 
    print ("\nAmarillo \n") 
    await asyncio.sleep(3)                												 #Espera a que cuente 3 para cambiar
    print ("Rojo \n")

async def S_horizontal():                 												 #Igual que la vertical
    print("\nVerde \n")
    task = asyncio.create_task(carros())   
    await asyncio.sleep(6)
    print ("\nAmarillo \n") 
    await asyncio.sleep(3)
    print ("Rojo \n") 

def U_input():
    print("Cúantos ciclos de semáforo: (24 seg por ciclo)")  		   #Pide al usuario el número de ciclos y maneja errores
    u_input = input()
    try:
        u_input = int(u_input)
    except: 
        print("Ingrese un número entero")
        U_input()
        return 0
    finally:
        if (u_input <= 0):
            print("Ingrese un número entero positivo\n")
            U_input()
        else:
            asyncio.run(Semaforo(u_input))    										 #Llama la función async desde una no async

U_input()
