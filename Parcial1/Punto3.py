import socket
import asyncio
import os

HOST = '127.0.0.1'
PORT = 65432

#directorio
os.chdir('/home/camilo/Documentos/HTML')

#Función para leer el html
async def lectura():
    with open('intro.html', 'r') as fp:
        pass
        a = fp.read()
    a = bytes(a,'utf-8')
    return a

async def connect():
    #empieza a leer el html
    task = asyncio.create_task(lectura())
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))            
        s.listen(2)                      
        conn, addr = s.accept()         
        with conn:                      
            print('Connected by', addr) 
            data = conn.recv(1024)
            #info de los bytes que se mandan
            conn.send(str.encode("HTTP/1.0 200 OK\n"))
            conn.send(str.encode('Content-Type: text/html\n'))
            #End of line sequence TELNET protocol
            conn.send(str.encode('\r\n')) 
            while True:     
                try:
                    #recibe la lectura del html
                    a = task.result()
                except:
                    #si no ha terminado optimiza para que los coprocesos sigan
                    await asyncio.sleep(0)
                    #print ('leyendo')
                else:
                    #una vez termina envía el html y cierra la conexión
                    conn.send(a)
                    print("Conexión terminada")
                    break


print("Esperando conexión")
asyncio.run(connect())
