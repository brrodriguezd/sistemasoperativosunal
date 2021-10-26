from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 
os.chdir(path)
  
with open('myfile.txt', 'w') as fp:
    pass
    fp.write("Documento")

path_archivo = 'D:/Estudio/Python/myfile.txt' 
status = os.stat(path_archivo) #Guarda el estado

print(status)             #Muestra todas las estadísticas 
print(status.st_size)     #Muestra una estadística específica

os.remove('myfile.txt')
