import os 

path = 'D:/Estudio/Python' 
os.chdir(path)
  
with open('myfile.txt', 'w') as fp:
    pass
    fp.write("Documento")

path_archivo = 'D:/Estudio/Python/myfile.txt' 
os.truncate(path_archivo, 3) #No deja que tenga más de 3 bytes de tamaño

with open('myfile.txt', 'r') as fp: 
    pass
    print(fp.read())  #el archivo solo deberia tener 3 letras
