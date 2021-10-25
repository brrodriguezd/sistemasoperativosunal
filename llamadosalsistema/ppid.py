from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
a = os.getppid()  #Obtiene el id del proceso padre

print (a)
