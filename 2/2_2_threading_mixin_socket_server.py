import os
import socket
import threading
import SocketServer

SERVER_HOST = "localhost"
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "Client received: %s" %response
    finally:
        sock.close()

class ThreadTCPRequesthandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s" %(current_thread.name,data)
        self.request.sendall(response)

class ThreadTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    server = ThreadTCPServer((SERVER_HOST,SERVER_PORT),ThreadTCPRequesthandler)
    ip,port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" %server_thread.name

    client(ip,port,"niconiconi~~~")
    client(ip,port,"LoveLive~~~")
    client(ip,port,"MoeSweetLolita~~~")

    server.shutdown()
