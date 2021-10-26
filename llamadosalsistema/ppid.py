from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
id_pp = os.getppid()  #Obtiene el id del proceso padre

print (id_pp)
