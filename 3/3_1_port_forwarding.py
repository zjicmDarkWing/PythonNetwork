import argparse

LOCAL_SERVER_HOST = "localhost"
REMOTE_SERVER_HOST = "localhost"
BUFSIZE = 4096

import asyncore
import socket

class PortForwarder(asyncore.dispatcher):
    def __init__(self,ip,port,remote_ip,remote_port,backlog=5):
        asyncore.dispatcher.__init__(self)
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip,port))
        self.listen(backlog)

    def handle_accept(self):
        conn,addr = self.accept()
        print "Connected to: %s" %addr
        Sender(Receiver(conn),self.remote_ip,self.remote_port)

class Receiver(asyncore.dispatcher):
    def __init__(self,conn):
        asyncore.dispatcher.__init__(self,conn)
        self.from_remote_buffer = ""
        self.to_remote_buffer = ""
        self.sender = None

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(BUFSIZE)
        self.from_remote_buffer += read

    def writable(self):
        return (len(self.to_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.to_remote_buffer)
        self.to_remote_buffer = self.to_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        if self.sender:
            self.sender.close()

class Sender(asyncore.dispatcher):
    def __init__(self,receiver,remote_addr,remote_port):
        asyncore.dispatcher.__init__(self)
        self.receiver = receiver
        receiver.sender = self
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect((remote_addr,remote_port))

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(BUFSIZE)
        self.receiver.to_remote_buffer += read

    def writable(self):
        return (len(self.receiver.from_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.receiver.from_remote_buffer)
        self.receiver.from_remote_buffer = self.receiver.from_remote_buffer[sent:]

    def handle_close(self):
        self.close()
        self.receiver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Stackless Socket Server Example")
    parser.add_argument("--local-host",action="store",dest="local_host",default=LOCAL_SERVER_HOST)
    parser.add_argument("--local-port",action="store",dest="local_port",type=int,required=True)
    parser.add_argument("--remote-host",action="store",dest="remote_host",default=REMOTE_SERVER_HOST)
    parser.add_argument("--remote-port",action="store",dest="remote_port",type=int,default=80)
    given_args = parser.parse_args()
    local_host = given_args.local_host
    local_port = given_args.local_port
    remote_host = given_args.remote_host
    remote_port = given_args.remote_port

    print "Starting port forwarding local %s:%s => remote %s:%s" \
          %(local_host,local_port,remote_host,remote_port)
    PortForwarder(local_host,local_port,remote_host,remote_port)
    asyncore.loop()
