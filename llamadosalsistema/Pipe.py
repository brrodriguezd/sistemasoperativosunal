from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
b = os.pipe() # Crea una tubería (método para pasar información de un proceso a otro), retorna una tupla con dos fd, para leer y editar respectivamente

print (b)
