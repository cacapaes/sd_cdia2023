import socket
import sys

def client(host, port, mensagem): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    try: 
        # Send data 
        print ("Sending %s" % mensagem) 
        sock.send(mensagem.encode('utf-8')) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 

if __name__ == '__main__':
    mensagem = sys.argv[1:]
    host = 'localhost'
    port=8082
    client(host,port,mensagem[0])