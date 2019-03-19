import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.1', 4444))
finish = True

while finish:
    client_data = raw_input("what do yo send?\n")
    if client_data.lower() == "bye":
        client_socket.send("bye")
        break
    '''
        enter flood attack here
    '''
    if True == False:
        break
    else:
        client_socket.send(client_data)
        data = client_socket.recv(2048)
        print "the server sent: " + data + "\n"


client_socket.close()

