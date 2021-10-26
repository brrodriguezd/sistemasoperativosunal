from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
b = os.pipe()

file = os.fdopen(b[0]) #regresa un archivo abierto conectado con el fd 

print (file)

file.close()
