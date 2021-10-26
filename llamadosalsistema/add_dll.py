from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
dll = os.add_dll_directory(path) #añade un path al busqueda de path del dll?
print (dll) #confirmacion
dll.close() #quita el directorio 
