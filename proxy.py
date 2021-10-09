import socket , sys , os 


port = 8888 #   port number
max_connection =  1 #   max nim of connections
buffer_size = 8192 

def start():
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', port)
        print("[*] Server started successfully  on {} :\nport {}".format(*server_address))

        # listen for incoming connections
        sock.listen(max_connection)
    except Exception:
        print("[*] Unable to Initialize Socket")
        print (Exception)
        sys.exit(-1)
    while True:
        try:
            connection , client_address = sock.accept() #   Accept connection from client browser
            data = connection.recv(buffer_size) #   Receive  client data 
        except KeyboardInterrupt:
            sock.close()
            print("[*] Shutdown\n")
            sys.exit(-1)
    sock.close()
    


