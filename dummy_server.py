# Start a listening server to simulate the behavior of the Unreal program.
import socket as S
import thread as T
import threading as TS

buffer_size = 1024
# host = '127.0.0.1'
host = '0.0.0.0'
port = 9000
client_socket = None

def handler(client_socket, client_address):
    print 'Client is connected'
    # while 1:
    #     data = client_socket.recv(buffer_size)
    #     print 'data:' + repr(data)
    #     # if not data: break # end of getting data
    #     client_socket.sendall("CaptureImage %s" % "real_scene.png")

def listen_server():
    endpoint = (host, port)
    server_socket = S.socket(S.AF_INET, S.SOCK_STREAM)
    server_socket.bind(endpoint)
    server_socket.listen(1) # Only allow one connection
    print 'Listening %s:%s' % (host, port)
    print 'Waiting for connection'
    global client_socket
    client_socket, client_address = server_socket.accept() # Block
    # Keep this socket alive until I explictly disconnect it
    print '... Connected from:', client_address
    T.start_new_thread(handler, (client_socket, client_address))

    # timer = TS.Timer(1, listen_server)
    # timer.start()

if __name__ == '__main__':
    listen_server()

    print 'Keep going on'
    while 1:
        message = raw_input('Type a message to send: ')
        print 'The message is: ', message
        client_socket.sendall(message) # Check whether this client is still connected?

    # Start a thread for interaction
