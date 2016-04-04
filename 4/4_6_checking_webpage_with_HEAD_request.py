#!/usr/bin/env python
# coding=utf-8

import argparse
import httplib
import urlparse
import re
import urllib

DEFAULT_URL = "http://zjicmisa.org"
HTTP_GOOD_CODES = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]


def get_server_status_code(url):
    print urlparse.urlparse(url)
    host, path = urlparse.urlparse(url)[1:3]
    print host, path
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example HEAD Request")
    parser.add_argument("--url", action="store", dest="url", default=DEFAULT_URL)
    given_args = parser.parse_args()
    url = given_args.url
    if get_server_status_code(url) in HTTP_GOOD_CODES:
        print "Server: %s status is OK" % url
    else:
        print "Server: %s status is NOT OK" % url
