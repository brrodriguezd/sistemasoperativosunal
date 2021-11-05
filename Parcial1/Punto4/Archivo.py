import os
import socket
import asyncio

HOST = '127.0.0.1'
PORT = 65432

os.chdir('/home/camilo/Documentos/Python')

with open('archivo.txt','w') as fp:
    pass
    fp.write("Archivo importante para pasar")

async def codificar():
    with open('archivo.txt','r') as fp:
        pass
        a = fp.read()
    a = bytes(a,'utf-8')
    return a

async def enviar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creates a socket
    s.connect((HOST, PORT))                                      #connects to the server   
    a = await codificar()
    s.send(a)                          
    print(a.decode('utf-8'))                                   #prints received data
    while True:
        data = s.recv(1024)
        if data == (b'f'):
            break
    s.close()

asyncio.run(enviar())
