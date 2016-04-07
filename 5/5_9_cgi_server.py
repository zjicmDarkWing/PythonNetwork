#!/usr/bin/env python
# coding=utf-8

import os
import cgi
import argparse
import BaseHTTPServer
import CGIHTTPServer
import cgitb

cgitb.enable()


def web_server(port):
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ("", port)
    handler.cgi_directories = ["/cgi-bin", ]
    httpd = server(server_address, handler)
    print "Starting web server with CGI support on port: %s" % port
    httpd.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CGI Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    web_server(port)
