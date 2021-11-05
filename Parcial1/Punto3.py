import socket
import asyncio
import os

HOST = '127.0.0.1'
PORT = 65432

#directorio
os.chdir('/home/camilo/Documentos/HTML')

with open('intro.html', 'w') as fp:
    pass
    fp.write(
"""<!DOCTYPE html> <!--declaration: this is an html5 document-->
<html lang="en"> <!--hyper text markup language-->
	<head>
		<title>Page title</title>
	</head>
	<body style="background-color:aliceblue;">
		<h1 style="text-align: center; color:green; background-color:rgba(253, 228, 184, 0.5); font-size:40px;"><!--from 1 to 6, 1 most important-->
			<i><ins>this is the header</ins></i> <!--emp emphasis--> <!--hsla(hue, color wheel, saturation, lightness, alpha)-->
		</h1>
		<p style="color:orange;">this is a paragrahp.</p> 
		<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/165px-Tux.svg.png">
			<b>This is a <small>small link</small></b>  <!--bold / <strong>--> 
		</a>
	</body>
</html>
"""
)
    
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
