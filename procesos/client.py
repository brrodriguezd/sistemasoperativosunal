import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def respuesta():
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
    while True:
        data = s.recv(1024)   
        if not data:
            break                             
        print(data.decode('utf-8'))                                   #prints received data
        answer = respuesta()
        s.sendall(answer)                                        #sends message 
    s.close()     
    