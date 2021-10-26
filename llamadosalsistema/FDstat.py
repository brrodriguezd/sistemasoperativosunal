from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)
  
fd = os.pipe()

fd_stat = os.fstat(fd[0])

print (fd_stat)
