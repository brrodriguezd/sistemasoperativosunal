from abc import abstractclassmethod
import os 

path = 'D:/Python'  #Directorio 
os.chdir(path)

dir_list = os.listdir(path)  #Guarda una lista de directorios, y archivos
print("Lista de archivos y directorios antes de crear:")
print(dir_list)
print ()
  
with open('myfile.txt', 'w') as fp: #Crea el archivo (w = solo escritura, r lectura, w+ escritura y lectura, a para concatenar, a+ para concatenar y leer) 
    pass
    fp.write("Nuevo documento") #Escribe en el archivo

dir_list = os.listdir(path) #Actualiza la lista de directorios
print("Lista de archivos y directorios despues de crear:")
print(dir_list)

os.remove('myfile.txt')
