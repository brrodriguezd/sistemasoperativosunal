import socket
import asyncio
#HTTPS
import ssl

HOST = 'www.buda.com'
PORT = 80
context = ssl.create_default_context()

with open('buda.txt', 'w') as fp:
    pass
a = ("GET /api/v2/markets HTTP/1.0\r\nHost: www.buda.com\r\n\r\n")
a = a.encode()

#TLS SSL para https

with socket.socket(socket.AF_INET ,socket.SOCK_STREAM) as s:
    print('connecting')
    with context.wrap_socket(s,server_hostname=HOST) as ssock:
        ssock.connect((HOST,PORT))
        print('connected')
        ssock.send(a)
        print('sending')
        while True:
            data = ssock.recv(1024)
            print(data)
            with open('buda.txt', 'a') as fp:
                pass                
                fp.write(str(data))
            if not data:
                break
