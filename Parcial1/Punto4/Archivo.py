import os
import socket
import asyncio

HOST = '127.0.0.1'
PORT = 65432

dir = '/home/camilo/Documentos/Python'
os.chdir(dir)
#Crea el archivo que va a pasar al cliente
with open('archivo.txt','w') as fp:
    pass
    fp.write("Crear archivo")

#Lee la dirección del directorio y scanea archivos .txt
async def codificar():
    a = ''
    with os.scandir(dir) as it:
        for entry in it: 
            if entry.is_file() and entry.name.endswith('.txt'):
                with open(entry,'r') as fp:
                    pass
										#Añade el nombre de los archivos y el contenido separado por ###
                    a = a + entry.name + '###' + fp.read()+ '###'
    #Convierte a bytes con encriptacion utf-8
	a = bytes(a,'utf-8')
    return a

async def enviar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.connect((HOST, PORT))   
    a = await codificar()
    s.send(a)                          
    print(a)                                   
    while True:
        data = s.recv(1024)
		#Espera a recibir f para acabar el programa
        if data == (b'f'):
            break
    s.close()

asyncio.run(enviar())
