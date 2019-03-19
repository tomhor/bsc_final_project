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
    server_data = client_server.recv(2048)
    counter = counter + 1
    if time.time() - start_time > 0.1:
        if counter > 100:
            client_server.close()
            server_socket.close()
        else:
            start_time = time.time()
            counter = 0

    server_data = server_data.lower()
    print "the client sent: " + server_data + "\n"
    if server_data == "time":
        client_server.send(str(datetime.now()))
    elif server_data == "name":
        client_server.send("my name is {}".format("Messi"))
    elif server_data == "id":
        client_server.send("my ID is 0000000000")
    elif server_data == "ip":
        client_server.send("my IP is {}".format(IP))
    elif server_data == "mygradeis":
        client_server.send("your grade is {}".format(str(random.randint(0,100))))
    elif server_data == "bye":
        finish = False
    else:
        client_server.send('I dont know what to do with: ' + server_data)

client_server.close()
server_socket.close()