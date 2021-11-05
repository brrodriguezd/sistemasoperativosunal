import os
import socket
import asyncio

HOST = '127.0.0.1'
PORT = 65432

dir = '/home/camilo/Documentos/Python'
os.chdir(dir)

with open('archivo.txt','w') as fp:
    pass
    fp.write("Crear archivo")
	
async def codificar():
    a = ''
    with os.scandir(dir) as it: #scandir(path) regresa un iterador 
        for entry in it: 
            if entry.is_file() and entry.name.endswith('.txt'):			#el método is_dir() regresa un valor booleano para determinar si entry es un directorio, mientras el método name.startswith('D') revisa que el directorio empiece con D 
                with open(entry,'r') as fp:
                    pass
                    a = a + entry.name + '###' + fp.read()+ '###'
    a = bytes(a,'utf-8')
    return a

async def enviar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creates a socket
    s.connect((HOST, PORT))                                      #connects to the server   
    a = await codificar()
    s.send(a)                          
    print(a)                                   #prints received data
    while True:
        data = s.recv(1024)
        if data == (b'f'):
            break
    s.close()

asyncio.run(enviar())
