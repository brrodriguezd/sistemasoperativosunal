from abc import abstractclassmethod
import os 

path = 'D:/Estudio/Python' 

os.chdir(path)

term_size = os.get_terminal_size() #Retorna el tamaño de la ventana de la terminal como (columnas, líneas)

print (term_size)
