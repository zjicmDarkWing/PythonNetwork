#!/usr/bin/env python
# coding=utf-8

import supervisor.xmlrpc
import xmlrpclib


def query_supervisor(sock):
    transport = supervisor.xmlrpc.SupervisorTransport(None, None, "unix://%s" % sock)
    proxy = xmlrpclib.ServerProxy("http://127.0.0.1", transport=transport)
    print "Getting info about all running processes via Supervisord..."
    print proxy.supervisor.getAllProcessInfo()


if __name__ == '__main__':
    query_supervisor(sock="/tmp/supervisor.sock")
