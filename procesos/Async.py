from abc import abstractclassmethod
import asyncio
from asyncio.tasks import sleep
import random

async def Semaforo(u_input):     
    for i in range (u_input):
        print ("Inicia el semáforo vertical (ciclo ", i+1, ")")       
        await S_vertical()                #Espera a que termina el semáforo vertical
        await asyncio.sleep(6)            #Cuenta el ciclo del semáforo en rojo
        print ("Inicia el semáforo horizontal")
        print ("\nAmarillo")
        await asyncio.sleep(3)            #Cuenta el ciclo de amarillo
        await S_horizontal()

async def carros():
    b = 0
    while b < 7:                          #Cuenta los segundos que tarda. El ciclo de verde tarda 6 segundos, por lo que hay una probabilidad de que alguien pase en amarillo mas no en rojo, añadido para más realismo xD
        a = random.randint(1,3)
        if a == 1:
            print ("paso un carro")
            b += 1
            await asyncio.sleep(1)        #Espera a que pase el vehículo
        elif a == 2:
            print ("paso un bus")
            b += 2
            await asyncio.sleep(2)
        elif a == 1:
            print ("paso un camión")
            b += 3
            await asyncio.sleep(3)

async def S_vertical():     
    print("\nVerde \n")
    task = asyncio.create_task(carros())  #Hace una tarea en simultaneo, que cuenta carros
    await asyncio.sleep(6)                #Espera a que cuente 7 para cambiar 
    print ("\nAmarillo \n") 
    await asyncio.sleep(3)                #Espera a que cuente 3 para cambiar
    print ("Rojo \n")

async def S_horizontal():                 #Igual que la vertical
    print("\nVerde \n")
    task = asyncio.create_task(carros())   
    await asyncio.sleep(6)
    print ("\nAmarillo \n") 
    await asyncio.sleep(3)
    print ("Rojo \n") 

def U_input():
    print("Cúantos ciclos de semáforo: ")  #Pide al usuario el número de ciclos y maneja errores
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
            asyncio.run(Semaforo(u_input))    #Llama la función async desde una no async

U_input()
