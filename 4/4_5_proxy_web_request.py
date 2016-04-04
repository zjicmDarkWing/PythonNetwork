#!/usr/bin/env python
# coding=utf-8

import urllib

URL = "url"
PROXY_ADDRESS = "proxy address"

if __name__ == '__main__':
    resp = urllib.urlopen(URL, proxies={"http": PROXY_ADDRESS})
    print "Proxy server returns response headers: %s" % resp.headers
