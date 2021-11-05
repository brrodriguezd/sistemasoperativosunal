import socket
import os
import asyncio

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

os.chdir('/home/camilo/Documentos/Python/FTP')

async def descifrar(a):
    a = a.decode('utf-8')
    print (a)                         
    return a

async def escribir(data):
    with open('archivo.txt', 'w') as fp:
        pass
        fp.write(data)
        
async def recibir():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(b'data2')                                      #connects to the server   
    data = s.recv(1024)   
    s.send(b'recibido')
    a = await descifrar(data)
    task = asyncio.create_task(escribir(a))
    while True:
        data = s.recv(1024)
        if data == (b'f'):
            break
    s.close()
        
asyncio.run(recibir())
