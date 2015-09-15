__author__ = 'DarkWing'

import socket

def convert_integer():
    data = 1234
    print "Original: %s => Long host byte order: %s,Network byte order: %s" \
          %(data,socket.ntohl(data),socket.htonl(data))
    print "Original: %s => Short host byte order: %s,Network byte order: %s" \
          %(data,socket.ntohs(data),socket.htons(data))

if __name__ == '__main__':
    convert_integer()