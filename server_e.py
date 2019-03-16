import socket
import time
import random
from datetime import datetime



print "waiting to client \n"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 4444))
server_socket.listen(1)
(client_server, (IP, port)) = server_socket.accept()
finish = True
start_time =time.time()
counter = 0
print "conected to IP: %s , port: %s \n" % (IP, port)

while finish:
    server_data = client_server.recv(2048) #the server is listening and wait for the client to send

    ''' 
        ENTER YOUR CODE HERE
    '''

client_server.close()
server_socket.close()