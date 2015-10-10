__author__ = 'DarkWing'

import socket
import sys
import argparse

host = "127.0.0.1"

def echo_client(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_address = (host,port)
    print "Connecting to %s port %s" %server_address
    sock.connect(server_address)

    try:
        message = "Test message.This will be echoed."
        print "Sending %s" %message
        sock.sendall(message)

        amount_received = 0
        amount_accepted = len(message)
        while amount_received < amount_accepted:
            data = sock.recv(16)
            amount_received += len(data)
            print "Received: %s" %data
    except socket.errno,e:
        print "Socket error: %s" %str(e)
    except Exception,e:
        print "Other exception: %s" %str(e)
    finally:
        print "Closing connection to the server"
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Client Example")
    parser.add_argument("--port",action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
