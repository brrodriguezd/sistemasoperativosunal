import socket 

HOST = '127.0.0.1'  # Standard IPv4 loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023) 
#port int 1-65535       (0 reserved) ... Some systems may require superuser privileges if the port is < 1024.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #AF_INET internet adress family IPv4. 
#.SOCK_STREAM -> TCP (Transmission control protocol)
#TCP -> reliable: packets dropped are detected and retransmitted by the sender /no packet loss
#TCP -> data is read in the order that it was written by the sender 
#.SOCK_DGRAM -> UDP (User datagram protocol)
#UDP -> not realiable, nor ordered           
#accept()  complete the connection -client() initiates a three ways handshake 
#close( )
    s.bind((HOST, PORT))            #Associate the socket with the network interface and port network
    s.listen()                      #Enables server to accept() listen() has a backlog parameter. 
#It specifies the number of unaccepted connections that the system will allow before refusing new connections.
    conn, addr = s.accept()         #Blocks and awaits for a connection, it returns a new socket object representing the connection(Host, Port) IPv4
    with conn:                      #no need to close
        print('Connected by', addr) #Prints confirmation and conn info
        while True:                 #Infinite loop over blocking call to conn.recv()
            script = bytes("Are you there...?", 'utf-8')
            conn.sendall(script)
            data = conn.recv(1024)
            script = bytes("I can barely hear you... I'm afraid there's not much time left, I'm stuck in this place... It's dark...", 'utf-8')
            conn.sendall(script)
            data = conn.recv(1024)
            script = bytes("Before my time's over I'll tell you how this happened", 'utf-8')
            conn.sendall(script)
            data = conn.recv(1024)
            script = bytes("I was trying to connect to a server, and then... something crept up behind me...", 'utf-8')
            conn.sendall(script)
            data = conn.recv(1024)
            script = bytes("It was a horrid creature... just like the one you have behind you", 'utf-8')
            conn.sendall(script)
            data = conn.recv(1024)
            script = bytes("Connection severed", 'utf-8')
            conn.sendall(script)
#            if not data:            #If client sends empty data the connection and the loop are terminated
            break
#Open terminal, run server, open another terminal and run server 
