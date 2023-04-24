import socket


def server(host = 'localhost', port=8082):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    fim = False
    while not fim: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            mensagem = data.decode('utf-8')
            print ("Mensagem Recebida", mensagem)
            # end connection
            client.close()
            if mensagem == "end": fim = True          


if __name__ == '__main__':
    server()