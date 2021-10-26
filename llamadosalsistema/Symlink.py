from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 
os.chdir(path)
  
#Requiere privilegios para funcionar
with open('src', 'w') as fp: #Crea el archivo para crear el symlink
    pass
    fp.write("Destino") 

src = 'D:/Estudio/Python/source'     
dst = 'D:/Estudio/Python/dest'     #Dirección del symlink que apunta a src

os.symlink(src, dst)
