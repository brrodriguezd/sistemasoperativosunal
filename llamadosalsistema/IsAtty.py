from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
fd = os.pipe()

isopen = os.isatty(fd[0]) #Retorna verdadero si esta abierto y conectado a un dispositivo de tipo tty 

print (isopen)
