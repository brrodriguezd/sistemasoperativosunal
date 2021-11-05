import socket
from os import chdir
import asyncio

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

chdir('/home/camilo/Documentos/Python')

async def descifrar(a):
    a = a.decode('utf-8')
    print (a)                         
    return a

async def escribir(data):
    info = data.split('###')
    for i in range (0,len(info)-1,2):
        with open(info[1], 'w') as fp:
            pass
            fp.write(info[i+1])
        
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
