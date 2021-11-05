import socket
import asyncio
import os

HOST = '127.0.0.1'
PORT = 65432

#directorio
os.chdir('/home/camilo/Documentos/Python')

async def descifrar(a):
    a = a.decode('utf-8')
    return a

async def mandar(conn, a):
    conn[0].send(a)

async def main():
    print("Esperando conexión")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))            
    s.listen(5)                      
    connection = s.accept() 
    print('Connected by', connection[1])             
    data = connection[0].recv(1024)
    tarea = asyncio.create_task(descifrar(data))
    connection2 = s.accept() 
    print('Connected by', connection2[1])             
    a = connection2[0].recv(1024)
    enviar = await mandar(connection2, data)
    a = connection2[0].recv(1024)
    terminar = asyncio.create_task(mandar(connection, (b'f')))
    task = asyncio.create_task(mandar(connection2, (b'f')))
    while True:
        try:
            a = terminar.result()
            a = task.result()
            data = tarea.result()
        except:
            await asyncio.sleep(0)
        else:
            break
    print("Conexión terminada")
    print(data)
    connection[0].close()
    connection2[0].close()
    s.close()

asyncio.run(main())
