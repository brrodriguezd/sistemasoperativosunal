from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
fd = os.pipe()

is_inheri = os.get_inheritable(fd[0]) #Informa si el fd es heredable

print (is_inheri)
