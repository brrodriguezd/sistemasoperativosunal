import socket

HOST = '127.0.0.1'  
PORT = 65432        

def respuesta():            #Datos codificados 
    a = input()
    if (a == ''):
        a = 'a'
    try:
        a = bytes(a, 'utf-8')
    except:
        a = respuesta()
    return a
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    #creates a socket
    s.connect((HOST, PORT))                                      #connects to the server   
    while True:                                                    #bucle para las multiples respuestas
        data = s.recv(1024)                                         #recibe datos
        if not data:                                                #si no recibe para el programa
            break                             
        print(data.decode('utf-8'))                                  #decodifica los mensajes
        answer = respuesta()                                         #recibe el input del usuario 
        s.sendall(answer)                                        #Manda el mensaje
    s.close()     
    
