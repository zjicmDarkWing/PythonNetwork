#!/usr/bin/env python
# encoding: utf-8

import SOAPpy

TEST_URL = "http://s3.amazonaws.com/ec2-downloads/2009-04-04.ec2.wsdl"


def list_soap_methods(url):
    proxy = SOAPpy.WSDL.Proxy(url)
    print "%d methods in WSDL:" % (len(proxy.methods)) + "\n"
    for key in proxy.methods.keys():
        print "Key Name: %s" % key
        print "Key Details:"
        for k, v in proxy.methods[key].__dict__.iteritems():
            print "%s ==> %s" % (k, v)
        break


if __name__ == '__main__':
    list_soap_methods(TEST_URL)
