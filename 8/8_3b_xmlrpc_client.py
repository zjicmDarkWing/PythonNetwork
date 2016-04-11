#!/usr/bin/env python
# coding=utf-8

import argparse
import xmlrpclib


def run_client(host, port, username, password):
    server = xmlrpclib.ServerProxy("http://%s:%s$%s:%s" % (username, password, host, port))
    msg = "niconiconi~~~"
    print "Sending message to server: %s" % msg
    print "Got reply: %s" % server.echo(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Multithreaded multicall XMLRPCServer/Proxy")
    parser.add_argument("--host", action="store", dest="host", default="127.0.0.1")
    parser.add_argument("--port", action="store", dest="port", default=8000, type=int)
    parser.add_argument("--username", action="store", dest="username", default="user")
    parser.add_argument("--password", action="store", dest="password", default="pass")
    given_args = parser.parse_args()
    host, port = given_args.host, given_args.port
    username, password = given_args.username, given_args.password
    run_client(host, port, username, password)
