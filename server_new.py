import socket
import select
import time
import random
from datetime import datetime

def send_waiting_messages(wlist1, messages_to_send1):
    for message in messages_to_send1:
        (client_socket, data) = message
        if client_socket in wlist1:
            client_socket.send(data)
            messages_to_send1.remove(message)



IP = '192.168.56.1' # TODO enter here your ip
server_socket = socket.socket()
server_socket.bind((IP, 4444))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []
numberOfClients = 0
counters = dict()
print 'server is running!! waiting for clients...'
while True:
    rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in rlist:
        if current_socket == server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
            counters[new_socket] = [0, time.time()]
            numberOfClients += 1
            print "connected to IP: %s , port: %s. number of clients is %s \n" % (address[0], address[1], numberOfClients)
        else:
            data = current_socket.recv(1024).lower()
            counters[current_socket][0] += 1
            if time.time() - counters[current_socket][1] > 0.1:
                if counters[current_socket][0]/float(time.time() - counters[current_socket][1]) > 1000:
                    open_client_sockets.remove(current_socket)
                    del counters[current_socket]
                    current_socket.close()
                    numberOfClients -= 1
                    print 'floodattack!! connection with a client is over. number of clients is {}\n'.format(str(numberOfClients))
                    continue
                else:
                    counters[current_socket][0] = 0
                    counters[current_socket][1] = time.time()
            if data == "bye":
                open_client_sockets.remove(current_socket)
                del counters[current_socket]
                numberOfClients -= 1
                print 'connection with a client is over. numebr of clients is {}\n'.format(str(numberOfClients))
            else:
                if data == "time":
                    messages_to_send.append((current_socket, 'the time is: '+str(datetime.now())))
                elif data == "details":
                    messages_to_send.append((current_socket, 'IP:{}, port:{}'.format(IP, "4444")))
                elif data == "grade":
                    messages_to_send.append((current_socket, 'my grade is {}'.format(str(random.randint(0, 100)))))
                elif data == "name":
                    messages_to_send.append(current_socket, 'my name is Messi')
                elif data == "id":
                    messages_to_send.append(current_socket, 'my id is 000000000')
                else:
                    messages_to_send.append((current_socket, 'I do not know what to do with: {}'.format(data)))

    send_waiting_messages(wlist, messages_to_send)