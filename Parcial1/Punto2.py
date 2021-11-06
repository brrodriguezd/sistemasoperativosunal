import socket
import asyncio
from os import chdir
#HTTPS
import ssl

chdir ('/home/camilo/Documentos/Python/Parcial1/Buda')

HOST = 'www.buda.com'
PORT = 443#HTTPS
context = ssl.create_default_context() 

async def conectarse(nombre, cmd):
    rec = ""
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        print('connecting')
        with context.wrap_socket(s, server_hostname=HOST) as ssock:
            ssock.connect((HOST,PORT))
            print('connected')
            ssock.send(cmd)
            #print('send')
            while True:
                data = ssock.recv(1024)
                #print (data)
                #decodifica y almacena
                rec = rec + data.decode('utf-8')
                #Fin del mensaje http 1.1, 1.0
                if data == b'0\r\n\r\n' or not data:
                    break
            #guarda en un .txt
            with open(nombre, 'w') as fp:
                pass                
                fp.write(rec)
            print ("conexión terminada")

async def main():
    cmd1 = (b'GET /api/v2/markets/eth-btc HTTP/1.1\r\nHost: www.buda.com\r\n\r\n')
    cmd2 = (b'GET /api/v2/currencies/eth/fees/deposit HTTP/1.0\r\nHost: www.buda.com\r\n\r\n')
    cmd3 = (b'GET /api/v2/markets/btc-clp/trades HTTP/1.0\r\nHost: www.buda.com\r\n\r\n')
    task1 = asyncio.create_task(conectarse('eth-btc.txt', cmd1))
    task2 = asyncio.create_task(conectarse('eth-fees.txt', cmd2))
    task3 = asyncio.create_task(conectarse('btc-clp-trades.txt', cmd3))

asyncio.run(main())